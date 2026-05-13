import sys
from PySide6.QtWidgets import (QApplication,QWidget, QLabel, QLineEdit, QTextBrowser,
                                QComboBox, QPushButton, QHBoxLayout, QDialog, QVBoxLayout)
from PySide6.QtCore import Slot

my_app = QApplication([])

class mainScreen(QWidget):
    def __init__(self):
        super().__init__()
        my_title = QLabel("Encrypter/Decrypter")

        self.linehere = QLineEdit()
        self.linehere.select_all()

        button = QPushButton("Search")
        button.clicked.connect(self.open)
        self.linehere.returnPressed.connect(self.open)

        self.mylabel = QLabel('')

        self.set_layout(vbox)
        self.show()
    
    @Slot()
    def open(self):
        looking = self.linehere.text
        mainpath = thesearch(looking)
