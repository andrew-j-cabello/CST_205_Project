import sys
from PySide6.QtWidgets import (QApplication,QWidget, QLabel, QLineEdit, QTextBrowser,
                                QComboBox, QPushButton, QHBoxLayout, QDialog, QVBoxLayout)
from PySide6.QtCore import Slot

my_app = QApplication([])

class mainScreen(QWidget):
    def __init__(self):
        super().__init__()
        my_title = QLabel("Encrypter/Decrypter")

        self.userline = QLineEdit("Please Enter A Search Term: ")
        self.userline.setMinimumWidth(250)
        self.userline.selectAll()

        button = QPushButton("Enter")
        self.label = QLabel("")

        button.clicked.connect(self.open)
        self.userline.returnPressed.connect(self.open)

        vbox = QVBoxLayout()
        vbox.addWidget(my_title)
        vbox.addWidget(self.userline)
        vbox.addWidget(button)
        vbox.addWidget(self.label)

        self.setLayout(vbox)
    
    @Slot()
    def open(self):
        your_input = self.userline.text()
        self.label.setText(f"Here's what you entered: {your_input}")


my_win = mainScreen()
my_win.show()

sys.exit(my_app.exec())
