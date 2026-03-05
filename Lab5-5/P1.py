"""
Pornsawan Khareram
683040156-9
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
    QLabel, QLineEdit, QDateEdit, QSpinBox,
    QPushButton, QDialog, QMessageBox, QScrollArea,
    QFrame, QSizePolicy
)
from PySide6.QtCore import Qt, Signal, QDate, QLocale
from PySide6.QtGui import QFont

class RoomCard(QWidget):
    """
    Room information card — Custom Widget Class
    """
    room_selected = Signal(str, int)

    def __init__(self, room_name: str, price: int, description: str, emoji: str = "🏨"):
        super().__init__()
        self._is_selected = False
        self.room_name = room_name
        self.price = price
        
        self._build_ui(emoji, description)
        self.deselect()

    def _build_ui(self, emoji: str, description: str):
        self.setFixedSize(200, 200)
        self.setCursor(Qt.PointingHandCursor)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(6)

        # Emoji Icon
        self.emoji_label = QLabel(emoji)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setFont(QFont("Segoe UI", 32))
        
        # Room Name
        self.name_label = QLabel(self.room_name)
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.name_label.setWordWrap(True)
        
        # Price
        self.price_label = QLabel(f"${self.price}/night")
        self.price_label.setAlignment(Qt.AlignCenter)
        self.price_label.setStyleSheet("color: #6366f1; font-weight: bold; font-size: 13px;")
        
        # Description
        self.desc_label = QLabel(description)
        self.desc_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setWordWrap(True)
        self.desc_label.setStyleSheet("color: #6b7280; font-size: 11px;")
        
        # Select Button
        self.select_btn = QPushButton("Select Room")
        self.select_btn.setCursor(Qt.PointingHandCursor)
        self.select_btn.clicked.connect(self._on_select_clicked)

        # Add to layout
        layout.addWidget(self.emoji_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.price_label)
        layout.addWidget(self.desc_label)
        layout.addStretch()
        layout.addWidget(self.select_btn)

    def _on_select_clicked(self):
        """When button is clicked, emit signal to notify parent"""
        self._is_selected = True
        self.room_selected.emit(self.room_name, self.price)

    def select(self):
        """Change to selected state (green border)"""
        self._is_selected = True
        self.setStyleSheet("""
            RoomCard {
                background-color: #f0fdf4;
                border: 2px solid #22c55e;
                border-radius: 12px;
            }
        """)
        self.select_btn.setStyleSheet("""
            QPushButton {
                background-color: #22c55e;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 5px;
                font-weight: bold;
            }
        """)
        self.select_btn.setText("✓ Selected")

    def deselect(self):
        """Change back to normal state"""
        self._is_selected = False
        self.setStyleSheet("""
            RoomCard {
                background-color: #ffffff;
                border: 2px solid #e5e7eb;
                border-radius: 12px;
            }
            RoomCard:hover {
                border: 2px solid #6366f1;
                background-color: #f5f3ff;
            }
        """)
        self.select_btn.setStyleSheet("""
            QPushButton {
                background-color: #6366f1;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 5px;
            }
            QPushButton:hover { background-color: #4f46e5; }
        """)
        self.select_btn.setText("Select Room")

    def is_selected(self):
        return self._is_selected
    

class ConfirmDialog(QDialog):
    """
    Booking confirmation popup
    """
    def __init__(self, guest_name: str, room_name: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Booking Confirmed")
        self.setFixedSize(360, 220)
        self.setModal(True)
        self._build_ui(guest_name, room_name)

    def _build_ui(self, guest_name: str, room_name: str):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(12)

        # Success Icon
        icon_label = QLabel("✅")
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setFont(QFont("Segoe UI", 40))
        
        # Title
        title = QLabel("Booking Successful!")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setStyleSheet("color: #16a34a;")
        
        # Message
        msg = QLabel(f"Dear {guest_name},\nthank you for booking the {room_name}.")
        msg.setAlignment(Qt.AlignCenter)
        msg.setStyleSheet("color: #374151; font-size: 13px;")
        msg.setWordWrap(True)
        
        # OK Button
        ok_btn = QPushButton("OK")
        ok_btn.setFixedHeight(36)
        ok_btn.setCursor(Qt.PointingHandCursor)
        ok_btn.setStyleSheet("""
            QPushButton {
                background-color: #22c55e;
                color: white;
                border: none;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #16a34a; }
        """)
        ok_btn.clicked.connect(self.accept)

        layout.addWidget(icon_label)
        layout.addWidget(title)
        layout.addWidget(msg)
        layout.addWidget(ok_btn)


# Booking Page

class BookingPage(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_room = None
        self.selected_price = 0
        self.cards = [] 
        self._build_ui()

    def _build_ui(self):
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)

        container = QWidget()
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(30, 24, 30, 24)
        main_layout.setSpacing(20)

        # Title
        title = QLabel("🏨 Book Your Stay at CozyStay")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setStyleSheet("color: #1e1b4b;")

        subtitle = QLabel("Fill in your details and choose your room")
        subtitle.setFont(QFont("Segoe UI", 10))
        subtitle.setStyleSheet("color: #6b7280;")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # Guest Info Form 
        form_title = QLabel("📋 Guest Information")
        form_title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        form_title.setStyleSheet("color: #374151; margin-top: 8px;")
        main_layout.addWidget(form_title)

        form_frame = QFrame()
        form_frame.setStyleSheet("""
            QFrame {
                background-color: #f9fafb;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        
        form_layout = QFormLayout(form_frame)
        form_layout.setSpacing(10)
        form_layout.setContentsMargins(15, 15, 15, 15)

        # Create widgets for inputs
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("e.g. John Smith")
        
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("e.g. 08x-xxx-xxxx")
        
        self.checkin_input = QDateEdit()
        self.checkin_input.setCalendarPopup(True)
        self.checkin_input.setDate(QDate.currentDate())
        self.checkin_input.setDisplayFormat("dd/MM/yyyy") 
        
        self.checkout_input = QDateEdit()
        self.checkout_input.setCalendarPopup(True)
        self.checkout_input.setDate(QDate.currentDate().addDays(1))
        self.checkout_input.setDisplayFormat("dd/MM/yyyy")
        
        self.guests_input = QSpinBox()
        self.guests_input.setRange(1, 20)
        self.guests_input.setValue(1)

        input_style = """
            QLineEdit, QDateEdit, QSpinBox {
                border: 1px solid #d1d5db;
                border-radius: 6px;
                padding: 6px 10px;
                font-size: 13px;
                background: white;
            }
            QLineEdit:focus, QDateEdit:focus, QSpinBox:focus {
                border: 1px solid #6366f1;
            }
        """
        for w in [self.name_input, self.phone_input,
                  self.checkin_input, self.checkout_input, self.guests_input]:
            w.setStyleSheet(input_style)
            w.setMinimumWidth(200)

        label_style = "font-size: 13px; color: #374151; font-weight: bold;"
        for text, widget in [
            ("Full Name :",       self.name_input),
            ("Phone Number :",    self.phone_input),
            ("Check-in Date :",   self.checkin_input),
            ("Check-out Date :",  self.checkout_input),
            ("Guests :",          self.guests_input),
        ]:
            lbl = QLabel(text)
            lbl.setStyleSheet(label_style)
            form_layout.addRow(lbl, widget)

        main_layout.addWidget(form_frame)

        # Room Selection
        room_title = QLabel("🛏 Select a Room")
        room_title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        room_title.setStyleSheet("color: #374151; margin-top: 8px;")
        main_layout.addWidget(room_title)

        rooms_data = [
            ("Standard Room", 50,  "Single bed, Free Wi-Fi",             "🛏"),
            ("Deluxe Room",   120, "Double bed, Ocean view, Wi-Fi",      "🌊"),
            ("Suite Room",    250, "Living room, Jacuzzi, Premium view", "👑"),
            ("Family Room",   160, "2 Bedrooms, Perfect for families",   "👨‍👩‍👧‍👦"),
        ]

        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(14)
        cards_layout.setContentsMargins(0, 0, 0, 0)

        for name, price, desc, emoji in rooms_data:
            card = RoomCard(name, price, desc, emoji)
            card.room_selected.connect(self._on_room_selected)
            self.cards.append(card)
            cards_layout.addWidget(card)

        cards_layout.addStretch()
        main_layout.addLayout(cards_layout)

        # Buttons 
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)

        self.clear_btn = QPushButton("🗑  Clear Info")
        self.clear_btn.setFixedHeight(42)
        self.clear_btn.setFont(QFont("Segoe UI", 11))
        self.clear_btn.setCursor(Qt.PointingHandCursor)
        self.clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #f3f4f6;
                color: #374151;
                border: 1px solid #d1d5db;
                border-radius: 8px;
                padding: 0 20px;
            }
            QPushButton:hover { background-color: #e5e7eb; }
        """)
        self.clear_btn.clicked.connect(self.clear_form)

        self.next_btn = QPushButton("Next  →")
        self.next_btn.setFixedHeight(42)
        self.next_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.next_btn.setCursor(Qt.PointingHandCursor)
        self.next_btn.setStyleSheet("""
            QPushButton {
                background-color: #6366f1;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0 28px;
            }
            QPushButton:hover { background-color: #4f46e5; }
        """)

        btn_layout.addWidget(self.clear_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(self.next_btn)

        main_layout.addLayout(btn_layout)
        main_layout.addStretch()

        scroll.setWidget(container)

        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(scroll)

    def _on_room_selected(self, room_name: str, price: int):
        """Receive signal from RoomCard, update state, deselect other cards"""
        self.selected_room = room_name
        self.selected_price = price
        
        for card in self.cards:
            if card.room_name != room_name:
                card.deselect()
            else:
                card.select()

    def clear_form(self):
        """Clear all form fields and deselect all room cards"""
        self.name_input.clear()
        self.phone_input.clear()
        self.checkin_input.setDate(QDate.currentDate())
        self.checkout_input.setDate(QDate.currentDate().addDays(1))
        self.guests_input.setValue(1)
        
        self.selected_room = None
        self.selected_price = 0
        
        for card in self.cards:
            card.deselect()

    def get_booking_data(self):
        """Collect form data — returns None if validation fails"""
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        checkin = self.checkin_input.date()
        checkout = self.checkout_input.date()
        guests = self.guests_input.value()

        if not name:
            QMessageBox.warning(self, "Missing Information", "Please enter your full name.")
            return None
        if not phone:
            QMessageBox.warning(self, "Missing Information", "Please enter your phone number.")
            return None
        if checkin >= checkout:
            QMessageBox.warning(self, "Invalid Dates",
                                "Check-out date must be after check-in date.")
            return None
        if not self.selected_room:
            QMessageBox.warning(self, "No Room Selected",
                                "Please select a room before proceeding.")
            return None

        nights = checkin.daysTo(checkout)
        total = nights * self.selected_price

        data_dict = {
            "name": name,
            "phone": phone,
            "checkin": checkin.toString("dd/MM/yyyy"),
            "checkout": checkout.toString("dd/MM/yyyy"),
            "guests": guests,
            "room": self.selected_room,
            "price": self.selected_price,
            "nights": nights,
            "total": total
        }

        return data_dict



# ReviewPage

class ReviewPage(QWidget):
    def __init__(self):
        super().__init__()
        self.current_data = {}
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(16)

        title = QLabel("📋 Booking Summary")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setStyleSheet("color: #1e1b4b;")

        subtitle = QLabel("Please review your details before confirming")
        subtitle.setFont(QFont("Segoe UI", 10))
        subtitle.setStyleSheet("color: #6b7280;")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        self.info_frame = QFrame()
        self.info_frame.setStyleSheet("""
            QFrame {
                background-color: #f9fafb;
                border-radius: 12px;
            }
        """)

        self.info_layout = QGridLayout(self.info_frame)
        self.info_layout.setSpacing(12)
        self.info_layout.setContentsMargins(20, 20, 20, 20)

        self.data_labels = {}

        display_keys = [
            ("🛏  Room", "room"),
            ("💰  Price / Night", "price"),
            ("👤  Guest Name", "name"),
            ("📞  Phone", "phone"),
            ("📅  Check-in", "checkin"),
            ("📅  Check-out", "checkout"),
            ("🌙  Nights", "nights"),
            ("👥  Guests", "guests"),
        ]

        key_style = "font-weight: bold; color: #374151; font-size: 13px;"
        val_style = "color: #1f2937; font-size: 13px;"

        for row, (key_text, dict_key) in enumerate(display_keys):
            key_lbl = QLabel(key_text)
            key_lbl.setStyleSheet(key_style)
            
            val_lbl = QLabel("-")
            val_lbl.setStyleSheet(val_style)
            val_lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            
            self.info_layout.addWidget(key_lbl, row, 0)
            self.info_layout.addWidget(val_lbl, row, 1)
            
            self.data_labels[dict_key] = val_lbl

        layout.addWidget(self.info_frame)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background-color: #e5e7eb;")
        layout.addWidget(line)

        total_layout = QHBoxLayout()
        total_key = QLabel("Total Amount")
        total_key.setFont(QFont("Segoe UI", 14, QFont.Bold))
        total_key.setStyleSheet("color: #1e1b4b;")
        
        self.total_label = QLabel("$ 0")
        self.total_label.setFont(QFont("Segoe UI", 14, QFont.Bold))
        self.total_label.setStyleSheet("color: #22c55e;")
        self.total_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        total_layout.addWidget(total_key)
        total_layout.addStretch()
        total_layout.addWidget(self.total_label)
        layout.addLayout(total_layout)

        layout.addStretch()

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)

        self.back_btn = QPushButton("←  Back")
        self.back_btn.setFixedHeight(44)
        self.back_btn.setFont(QFont("Segoe UI", 11))
        self.back_btn.setCursor(Qt.PointingHandCursor)
        self.back_btn.setStyleSheet("""
            QPushButton {
                background-color: #f3f4f6;
                color: #374151;
                border: 1px solid #d1d5db;
                border-radius: 8px;
                padding: 0 22px;
            }
            QPushButton:hover { background-color: #e5e7eb; }
        """)

        self.submit_btn = QPushButton("✅  Confirm Booking")
        self.submit_btn.setFixedHeight(44)
        self.submit_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.submit_btn.setCursor(Qt.PointingHandCursor)
        self.submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #22c55e;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0 28px;
            }
            QPushButton:hover { background-color: #16a34a; }
        """)

        btn_layout.addWidget(self.back_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(self.submit_btn)
        layout.addLayout(btn_layout)

    def load_data(self, data: dict):
        """Receive data dict from BookingPage and populate the review layout"""
        self.current_data = data
        
        self.data_labels["room"].setText(data.get("room", "-"))
        self.data_labels["price"].setText(f"${data.get('price', 0)}")
        self.data_labels["name"].setText(data.get("name", "-"))
        self.data_labels["phone"].setText(data.get("phone", "-"))
        self.data_labels["checkin"].setText(data.get("checkin", "-"))
        self.data_labels["checkout"].setText(data.get("checkout", "-"))
        self.data_labels["nights"].setText(f"{data.get('nights', 0)} night(s)")
        self.data_labels["guests"].setText(f"{data.get('guests', 0)} guest(s)")
        
        self.total_label.setText(f"$ {data.get('total', 0)}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CozyStay — Hotel Booking System")
        self.setMinimumSize(820, 680)
        self.resize(900, 720)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.booking_page = BookingPage()
        self.review_page = ReviewPage()

        self.stack.addWidget(self.booking_page)
        self.stack.addWidget(self.review_page)

        self.booking_page.next_btn.clicked.connect(self._go_to_review)
        self.review_page.back_btn.clicked.connect(self._go_to_booking)
        self.review_page.submit_btn.clicked.connect(self._on_submit)

        self.stack.setCurrentIndex(0)

        self.setStyleSheet("""
            QMainWindow { background-color: #f0f0ff; }
            QScrollArea  { background-color: transparent; }
            QWidget      { font-family: 'Segoe UI', 'Tahoma', sans-serif; }
        """)

    def _go_to_review(self):
        data = self.booking_page.get_booking_data()
        if data is None:
            return
        self.review_page.load_data(data)
        self.stack.setCurrentIndex(1)

    def _go_to_booking(self):
        self.stack.setCurrentIndex(0)

    def _on_submit(self):
        guest_name = self.review_page.current_data.get("name", "Guest")
        room_name = self.review_page.current_data.get("room", "Room")
        
        dialog = ConfirmDialog(guest_name, room_name, self)
        dialog.exec()
        
        self.booking_page.clear_form()
        self.stack.setCurrentIndex(0)


def main():
    app = QApplication(sys.argv)
    
    # --- FIX: Force Arabic Numerals (0-9) ---
    # Setting locale to English (UK) ensures Arabic numerals and dd/MM/yyyy format.
    # You can also use QLocale(QLocale.English, QLocale.UnitedStates) for MM/dd/yyyy.
    QLocale.setDefault(QLocale(QLocale.English, QLocale.UnitedKingdom))
    # ----------------------------------------
    
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()