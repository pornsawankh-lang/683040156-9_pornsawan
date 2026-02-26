"""
Pornsawan Khareram
683040156-9
"""
import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QLineEdit, QPushButton,
    QComboBox, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout,
    QHBoxLayout, QGridLayout, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class StudentGradeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: Student scores and grades")
        self.setMinimumSize(1000, 600)

        self.students = {}
        self.load_students()

        self.init_ui()
        self.apply_style()

    def load_students(self):
        if not os.path.exists("students.txt"):
            QMessageBox.warning(self, "Error", "students.txt not found")
            return

        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    sid, name = line.split(",")
                    self.students[sid] = name

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()

        # TOP SECTION
        top_layout = QGridLayout()

        # Student ID
        self.id_combo = QComboBox()
        self.id_combo.addItem("Select Student ID")
        self.id_combo.addItems(sorted(self.students.keys()))
        self.id_combo.currentTextChanged.connect(self.update_name)

        # Student Name
        self.name_edit = QLineEdit()
        self.name_edit.setReadOnly(True)

        # Scores
        self.math_input = QSpinBox()
        self.math_input.setRange(0, 100)

        self.science_input = QSpinBox()
        self.science_input.setRange(0, 100)

        self.english_input = QSpinBox()
        self.english_input.setRange(0, 100)

        # Layout arrangement 
        top_layout.addWidget(QLabel("Student ID:"), 0, 0)
        top_layout.addWidget(self.id_combo, 0, 1)

        top_layout.addWidget(QLabel("Student Name:"), 0, 3)
        top_layout.addWidget(self.name_edit, 0, 4, 1, 3)

        top_layout.addWidget(QLabel("Math:"), 1, 0)
        top_layout.addWidget(self.math_input, 1, 1)

        top_layout.addWidget(QLabel("Science:"), 1, 2)
        top_layout.addWidget(self.science_input, 1, 3)

        top_layout.addWidget(QLabel("English:"), 1, 4)
        top_layout.addWidget(self.english_input, 1, 5)

        # BUTTON SECTION
        button_layout = QHBoxLayout()

        self.add_btn = QPushButton("Add Student")
        self.reset_btn = QPushButton("Reset Input")
        self.clear_btn = QPushButton("Clear All")

        self.add_btn.clicked.connect(self.add_student)
        self.reset_btn.clicked.connect(self.reset_input)
        self.clear_btn.clicked.connect(self.clear_all)

        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.reset_btn)
        button_layout.addWidget(self.clear_btn)

        self.table = QTableWidget()
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels([
            "No.", "Student ID", "Name",
            "Math", "Science", "English",
            "Total", "Average", "Grade"
        ])

        main_layout.addLayout(top_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.table)

        central.setLayout(main_layout)

    def update_name(self):
        sid = self.id_combo.currentText()
        if sid in self.students:
            self.name_edit.setText(self.students[sid])
        else:
            self.name_edit.clear()

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

    def add_student(self):
        sid = self.id_combo.currentText()
        if sid not in self.students:
            return

        name = self.name_edit.text()
        m = self.math_input.value()
        s = self.science_input.value()
        e = self.english_input.value()

        total = m + s + e
        avg = total / 3
        grade = self.calculate_grade(avg)

        row = self.table.rowCount()
        self.table.insertRow(row)

        values = [
            str(row + 1),
            sid,
            name,
            str(m),
            str(s),
            str(e),
            str(total),
            f"{avg:.2f}",
            grade
        ]

        for col, val in enumerate(values):
            item = QTableWidgetItem(val)
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, col, item)

        for col, score in zip([3, 4, 5], [m, s, e]):
            if score < 50:
                self.table.item(row, col).setBackground(QColor("#f8c8c8"))

        if grade == "A":
            self.table.item(row, 8).setBackground(QColor("#c8f7c5"))
        elif grade == "F":
            self.table.item(row, 8).setBackground(QColor("#f8c8c8"))

        self.sort_table()

    def sort_table(self):
        self.table.sortItems(1, Qt.AscendingOrder)

        for row in range(self.table.rowCount()):
            self.table.setItem(row, 0, QTableWidgetItem(str(row + 1)))

    def reset_input(self):
        self.math_input.setValue(0)
        self.science_input.setValue(0)
        self.english_input.setValue(0)

    def clear_all(self):
        self.table.setRowCount(0)

    def apply_style(self):
        self.setStyleSheet("""
        QMainWindow {
            background-color: #e6e6e6;
        }

        QLabel {
            font-size: 13px;
        }

        QLineEdit {
            background-color: #f6f1dd;
            padding: 5px;
        }

        QSpinBox, QComboBox {
            padding: 4px;
        }

        QPushButton {
            background-color: #5da9dd;
            color: white;
            padding: 10px;
            font-weight: bold;
            border-radius: 5px;
        }

        QPushButton:hover {
            background-color: #4b94c8;
        }

        QTableWidget {
            background-color: white;
        }

        QHeaderView::section {
            background-color: #f0f0f0;
            font-weight: bold;
        }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentGradeApp()
    window.show()
    sys.exit(app.exec())