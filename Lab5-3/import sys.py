import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QLabel, QComboBox, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class GradeCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Grade Calculator")
        self.setGeometry(200, 100, 850, 600)

        self.students = {}  # {id: name}

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        self.create_input_section()
        self.create_buttons()
        self.create_table()
        self.load_students()

        self.apply_styles()

    # ===============================
    # Load students from file
    # ===============================
    def load_students(self):
        try:
            with open("students.txt", "r") as file:
                for line in file:
                    student_id, name = line.strip().split(",")
                    self.students[student_id] = name
                    self.id_combo.addItem(student_id)
        except:
            QMessageBox.warning(self, "Error", "students.txt not found.")

    # ===============================
    # Input Section
    # ===============================
    def create_input_section(self):
        grid = QGridLayout()
        self.main_layout.addLayout(grid)

        grid.addWidget(QLabel("Student ID:"), 0, 0)
        self.id_combo = QComboBox()
        self.id_combo.currentTextChanged.connect(self.update_name)
        grid.addWidget(self.id_combo, 0, 1)

        grid.addWidget(QLabel("Student Name:"), 1, 0)
        self.name_label = QLabel("")
        grid.addWidget(self.name_label, 1, 1)

        grid.addWidget(QLabel("Math Score:"), 2, 0)
        self.math_input = QLineEdit()
        grid.addWidget(self.math_input, 2, 1)

        grid.addWidget(QLabel("Science Score:"), 3, 0)
        self.science_input = QLineEdit()
        grid.addWidget(self.science_input, 3, 1)

        grid.addWidget(QLabel("English Score:"), 4, 0)
        self.english_input = QLineEdit()
        grid.addWidget(self.english_input, 4, 1)

    # ===============================
    # Buttons
    # ===============================
    def create_buttons(self):
        btn_layout = QHBoxLayout()
        self.main_layout.addLayout(btn_layout)

        self.add_btn = QPushButton("Add Student")
        self.reset_btn = QPushButton("Reset Input")
        self.clear_btn = QPushButton("Clear All")

        self.add_btn.clicked.connect(self.add_student)
        self.reset_btn.clicked.connect(self.reset_inputs)
        self.clear_btn.clicked.connect(self.clear_table)

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.reset_btn)
        btn_layout.addWidget(self.clear_btn)

    # ===============================
    # Table
    # ===============================
    def create_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "Student ID", "Name",
            "Math", "Science", "English",
            "Total", "Average", "Grade"
        ])
        self.main_layout.addWidget(self.table)

    # ===============================
    # Update Name Automatically
    # ===============================
    def update_name(self, student_id):
        if student_id in self.students:
            self.name_label.setText(self.students[student_id])

    # ===============================
    # Add Student
    # ===============================
    def add_student(self):
        try:
            student_id = self.id_combo.currentText()
            name = self.name_label.text()

            math = float(self.math_input.text())
            science = float(self.science_input.text())
            english = float(self.english_input.text())

            for score in [math, science, english]:
                if score < 0 or score > 100:
                    raise ValueError("Scores must be between 0 and 100.")

            total = math + science + english
            average = total / 3
            grade = self.calculate_grade(average)

            self.insert_sorted_row(
                student_id, name,
                math, science, english,
                total, round(average, 2), grade
            )

        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))
        except:
            QMessageBox.warning(self, "Input Error", "Please enter valid scores.")

        grade_item = QTableWidgetItem(grade)
        grade_item.setTextAlignment(Qt.AlignCenter)

        if grade == "A":
            grade_item.setBackground(QColor("#4bad44"))  # green
        elif grade == "F":
            grade_item.setBackground(QColor("#a23030"))  # red

        self.table.setItem(row, 7, grade_item)

        self.sort_table()

    # ===============================
    # Insert Row Sorted by ID
    # ===============================
    def insert_sorted_row(self, *data):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        for column, value in enumerate(data):
            self.table.setItem(row_position, column, QTableWidgetItem(str(value)))

        self.table.sortItems(0, Qt.AscendingOrder)

    # ===============================
    # Grade Calculation
    # ===============================
    def calculate_grade(self, avg):
        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    # ===============================
    # Reset Inputs
    # ===============================
    def reset_inputs(self):
        self.math_input.clear()
        self.science_input.clear()
        self.english_input.clear()

    # ===============================
    # Clear Table
    # ===============================
    def clear_table(self):
        self.table.setRowCount(0)

    # ===============================
    # Styling (QSS)
    # ===============================
    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f4f6f8;
            }
            QLabel {
                font-size: 14px;
            }
            QLineEdit, QComboBox {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            QPushButton {
                padding: 8px;
                background-color: #4A90E2;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #357ABD;
            }
            QTableWidget {
                background-color: white;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradeCalculator()
    window.show()
    sys.exit(app.exec())