"""CSC111 Winter 2023 Final Project: ScreenSelect
===============================

This file contains the classes and main to run the
unconnected GUI for ScreenSelect.

Copyright and Usage Information
===============================
This file is provided solely for the use of marking the project to the
staff of CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.
This file is Copyright (c) 2023 Aastha Sharma, Sidharth Sawhney,
Narges Movahedian Nezhad, and Dogyu Lee.
"""
from typing import Any

from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
import sys


class RecommendationScreen(QWidget):
    """The third screen the user sees, also where they choose a recommended movie given.

    If the ScreenSelect button or Back is clicked then it takes the user back to Prefernce screen.
    """
    def __init__(self, movie_lst: dict[int, Any]) -> None:
        super().__init__()
        self.movie_lst = movie_lst
        self.w = None
        layout = QGridLayout()
        self.setWindowIcon(QIcon("ScreenSelectIcon.jpg"))
        self.setStyleSheet("background-color: #CAD7CF;")

        self.setWindowTitle("ScreenSelect")
        self.setLayout(layout)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        title1 = QLabel("ScreenSelect: Personalized Movie Recommendation System")
        title1.setStyleSheet("color: #347c99;")
        title1.setFont(QFont("Trebuchet MS", 20, QFont.Weight.Bold))
        layout.addWidget(title1, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        colum = 0
        for movie in movie_lst:
            save = str(movie_lst[movie])
            movie1 = QLabel(save)
            movie1.setFont(QFont("Courier New", 15))
            movie1.setStyleSheet("color: #347c99;")
            layout.addWidget(movie1, 3, colum, 1, 3)
            button1 = QPushButton("ScreenSelect")
            button1.setFont(QFont("Courier New", 12))
            button1.setStyleSheet("background-color: #347c99; color: #FFFFFF;")
            button1.clicked.connect(self.screenselect)
            layout.addWidget(button1, 4, colum)
            colum += 1
        button2 = QPushButton("Back")
        button2.setFont(QFont("Courier New", 12))
        button2.setStyleSheet("background-color: #347c99; color: #FFFFFF;")
        button2.clicked.connect(self.back)
        layout.addWidget(button2)

    def screenselect(self):
        """
        Select one of the given movies and add it to graph neighbours,
        then return back to the preferences screen.
        """
        # sid do the work function call
        if self.w is None:
            self.w = PrefenceScreen()
        self.w.show()
        self.close()

    def back(self):
        """
        Without selecting a movie return to the preferences screen.
        """
        if self.w is None:
            self.w = PrefenceScreen()
        self.w.show()
        self.close()


class PrefenceScreen(QWidget):
    """The second screen the user sees, also where they put in their preferences and
    the button - Recommendations is clicked to go to next screen

    If the Logout button is clicked then the system goes back to the LogInScreen page.
    """

    def __init__(self) -> None:
        super().__init__()
        self.w = None
        layout = QGridLayout()
        self.setWindowIcon(QIcon("ScreenSelectIcon.jpg"))
        self.setStyleSheet("background-color: #CAD7CF;")

        self.setWindowTitle("ScreenSelect")
        self.setLayout(layout)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)
        title1 = QLabel("ScreenSelect: Personalized Movie Recommendation System")
        title1.setStyleSheet("color: #347c99;")
        title1.setFont(QFont("Trebuchet MS", 20, QFont.Weight.Bold))
        layout.addWidget(title1, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        title2 = QLabel("Add the Movie Preferences:")
        title2.setStyleSheet("color: #347c99;")
        title2.setFont(QFont("Trebuchet MS", 16, QFont.Weight.Bold))
        layout.addWidget(title2, 2, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

        genre = QLabel("Genre:")
        genre.setFont(QFont("Courier New", 15))
        genre.setStyleSheet("color: #347c99;")
        layout.addWidget(genre, 3, 0)
        lang = QLabel("Language:")
        lang.setFont(QFont("Courier New", 15))
        lang.setStyleSheet("color: #347c99;")
        layout.addWidget(lang, 4, 0)
        key = QLabel("Keywords (max 3):")
        key.setFont(QFont("Courier New", 15))
        key.setStyleSheet("color: #347c99;")
        layout.addWidget(key, 5, 0)
        director = QLabel("Director:")
        director.setFont(QFont("Courier New", 15))
        director.setStyleSheet("color: #347c99;")
        layout.addWidget(director, 8, 0)

        self.genre_input = QLineEdit()
        self.genre_input.setStyleSheet("background-color: #FFFFFF;")  # Set input background color
        self.genre_input.setFont(QFont("Arial", 12))
        layout.addWidget(self.genre_input, 3, 1, 1, 2)
        self.lang_input = QLineEdit()
        self.lang_input.setStyleSheet("background-color: #FFFFFF;")  # Set input background color
        self.lang_input.setFont(QFont("Arial", 12))
        layout.addWidget(self.lang_input, 4, 1, 1, 2)
        self.key_input1 = QLineEdit()
        self.key_input1.setStyleSheet("background-color: #FFFFFF;")  # Set input background color
        self.key_input1.setFont(QFont("Arial", 12))
        layout.addWidget(self.key_input1, 5, 1, 1, 2)
        self.key_input2 = QLineEdit()
        self.key_input2.setStyleSheet("background-color: #FFFFFF;")  # Set input background color
        self.key_input2.setFont(QFont("Arial", 12))
        layout.addWidget(self.key_input2, 6, 1, 1, 2)
        self.key_input3 = QLineEdit()
        self.key_input3.setStyleSheet("background-color: #FFFFFF;")  # Set input background color
        self.key_input3.setFont(QFont("Arial", 12))
        layout.addWidget(self.key_input3, 7, 1, 1, 2)
        self.director_input = QLineEdit()
        self.director_input.setStyleSheet("background-color: #FFFFFF;")  # Set input background color
        self.director_input.setFont(QFont("Arial", 12))
        layout.addWidget(self.director_input, 8, 1, 1, 2)

        button1 = QPushButton("Log Out")  # calling the sign in function
        button1.setFont(QFont("Courier New", 12))
        button1.setStyleSheet("background-color: #347c99; color: #FFFFFF;")
        button1.clicked.connect(self.log_out)
        layout.addWidget(button1, 9, 1)

        button2 = QPushButton("Recommend")  # calling the sign in function
        button2.setFont(QFont("Courier New", 12))
        button2.setStyleSheet("background-color: #347c99; color: #FFFFFF;")
        button2.clicked.connect(self.recommendation_button)
        layout.addWidget(button2, 9, 2)

    def log_out(self):
        """
        Function activated when button1 clicked, takes back to the LogInScreen.
        """
        if self.w is None:
            self.w = LogInScreen()
        self.w.show()
        self.close()

    def recommendation_button(self):
        """
        Function activated when button2 clicked, takes to the Recommendation screen.
        """
        if self.w is None:
            self.w = RecommendationScreen({1: 'Aastha', 2: 'Narges', 3: 'Dorothy', 4: 'Sid', 5: 'ScreenSelect'})
            # call the function that gives the 5 movies to present
            # Don't forgot to change the recommendation system innit SID do the work
        self.w.show()
        self.close()


class LogInScreen(QWidget):
    """The Log in window that the user sees once the movies are all loaded up in the graph.

    The user can sign up or sign in. When the cross on top is pressed the code stops running and stops.

    Input is only the username, possible buttons are sign up or sign in.
    """

    def __init__(self) -> None:
        super().__init__()
        self.w = None
        layout = QGridLayout()
        self.setWindowIcon(QIcon("ScreenSelectIcon.jpg"))
        self.setStyleSheet("background-color: #CAD7CF;")

        self.setWindowTitle("ScreenSelect")
        self.setLayout(layout)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)
        title = QLabel("ScreenSelect: Personalized Movie Recommendation System")
        title.setStyleSheet("color: #347c99;")
        title.setFont(QFont("Trebuchet MS", 20, QFont.Weight.Bold))
        layout.addWidget(title, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

        user = QLabel("Username:")
        user.setFont(QFont("Courier New", 15))
        user.setStyleSheet("color: #347c99;")
        layout.addWidget(user, 1, 0)

        self.input1 = QLineEdit()
        self.input1.setStyleSheet("background-color: #FFFFFF;")  # Set input background color
        self.input1.setFont(QFont("Arial", 12))
        layout.addWidget(self.input1, 1, 1, 1, 2)

        button1 = QPushButton("Sign In")
        button1.setFont(QFont("Courier New", 12))
        button1.setStyleSheet("background-color: #347c99; color: #FFFFFF;")
        button1.clicked.connect(self.sign_in)  # calling the sign in function
        layout.addWidget(button1, 3, 1)

        button2 = QPushButton("Sign Up")
        button2.setFont(QFont("Courier New", 12))
        button2.setStyleSheet("background-color: #347c99; color: #FFFFFF;")
        button2.clicked.connect(self.sign_up)  # calling the sign in function
        layout.addWidget(button2, 3, 2)

    def sign_in(self):
        """
        if self.input1 in #graph._vertices:
            call function and move to next screen - preferences
        else:
            print("Please sign up")
        """
        print('correct call reached sign in')
        # Sid Implement THIS
        if self.w is None:
            self.w = PrefenceScreen()
        self.w.show()
        self.close()

    def sign_up(self):
        """
        if self.input1 in #graph._vertices:
            print('Invalid Username')
        else:
            # call function and move to next screen - preferences
        """
        print('correct call reached sign up')
        if self.w is None:
            self.w = PrefenceScreen()
        self.w.show()
        self.close()
        # Sid Implement THIS


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogInScreen()
    window.show()  # To show the gui window the above code is very static to a window open
    sys.exit(app.exec())


