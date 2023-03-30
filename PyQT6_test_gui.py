"""Trying GUI application"""
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout)
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    """The window for GUI.
    """

    def __init__(self) -> None:
        super().__init__()
        layout = QGridLayout()

        self.setWindowTitle("ScreenSelect")
        self.setLayout(layout)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)
        title = QLabel("ScreenSelect: Personalized Movie Recommendation System")
        layout.addWidget(title, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

        user = QLabel("Username:")
        layout.addWidget(user, 1, 0)

        self.input1 = QLineEdit()
        layout.addWidget(self.input1, 1, 1, 1, 2)

        button1 = QPushButton("Sign In")
        button1.clicked.connect(self.login)  # calling the sign in function
        layout.addWidget(button1, 3, 1)

    def login(self):
        """ login funvction"""
        if self.input1.text() == "Aastha":
            print("username and pasword correct")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()  # To show the gui window the above code is very static to a window open
    sys.exit(app.exec())

#  only impors will change the above will stay static
