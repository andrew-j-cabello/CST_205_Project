import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                                QVBoxLayout)
from PySide6.QtCore import Slot

from Decrypter import connect

my_app = QApplication([])

class mainScreen(QWidget):
    def __init__(self):
        super().__init__()
        my_title = QLabel("Encrypter/Decrypter")

        self.userline = QLineEdit()
        self.userline.setPlaceholderText("Image to hide")

        self.cryptline = QLineEdit()
        self.cryptline.setPlaceholderText("cover img")
    

        button = QPushButton("Enter")
        self.label = QLabel("")

        button.clicked.connect(self.open)

        vbox = QVBoxLayout()
        vbox.addWidget(my_title)
        vbox.addWidget(self.userline)
        vbox.addWidget(self.cryptline)
        vbox.addWidget(button)
        vbox.addWidget(self.label)

        self.setLayout(vbox)
    
    @Slot()
    def open(self):
        p = self.userline.text().strip()
        p2 = self.cryptline.text().strip()

        if not p or not p2:
            self.label.setText("Enter image desc.")
            print("[gui] Need both fields: secret query and cover query.")
            return

        print(f"[gui] Run: hide={p!r}, cover={p2!r}")
        self.label.setText("Working")
        try:
            connect(p, p2)
            self.label.setText("Finished")
            print("[gui] Done.")
        except Exception as e:
            self.label.setText(f"Fail: {e}")
            print(f"[gui] Error: {e}")


my_win = mainScreen()
my_win.show()
sys.exit(my_app.exec())
