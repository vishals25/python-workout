from PyQt6.QtWidgets import QApplication,QLabel,QGridLayout
from PyQt6.QtWidgets import QWidget,QPushButton,QLabel,QLineEdit
import sys
from datetime import datetime

class AgeCalculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid=QGridLayout()

        name_label=QLabel("Name of Student:")
        self.name_line_edit=QLineEdit()

        dob_label=QLabel("Date of Birth(DD/MM/YYYY):")
        self.dob_line_edit=QLineEdit()

        calculate_button=QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label=QLabel("")

        grid.addWidget(name_label,0,0)
        grid.addWidget(self.name_line_edit,0,1)
        grid.addWidget(dob_label,1,0)
        grid.addWidget(self.dob_line_edit,1,1)
        grid.addWidget(calculate_button,2,0,1,2)
        grid.addWidget(self.output_label,3,0,1,2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year=datetime.now().year
        dob=self.dob_line_edit.text()
        yob=datetime.strptime(dob,"%d/%m/%Y").date().year
        age=current_year-yob
        self.output_label.setText(f"Name = {self.name_line_edit.text()}\nAge  = {age}")


app=QApplication(sys.argv)
age_calculator=AgeCalculator()
age_calculator.show()
sys.exit(app.exec())