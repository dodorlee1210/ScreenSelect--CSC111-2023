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
from PyQt6.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QGridLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from classes import Graph, _User, _Movie
import main_functions


class RecommendationScreen(QWidget):
    """The third screen the user sees, also where they choose a recommended movie given.
    If the ScreenSelect button or Back is clicked then it takes the user back to Prefernce screen.
    """

    def __init__(self, top_scores: list[tuple[int, _Movie]], graph: Graph, user_obj: _User) -> None:
        super().__init__()
        self.graph = graph
        self.user_obj = user_obj
        self.movie_lst = top_scores

        self.w = None
        layout = QGridLayout()
        self.setWindowIcon(QIcon("ScreenSelectIcon.jpg"))
        self.setStyleSheet("background-color: #CAD7CF;")

        self.setWindowTitle("ScreenSelect")
        self.setLayout(layout)
        layout.setContentsMargins(60, 60, 60, 60)
        title1 = QLabel("ScreenSelect: Personalized Movie Recommendation System")
        title1.setStyleSheet("color: #347c99;")
        title1.setFont(QFont("Trebuchet MS", 20, QFont.Weight.Bold))
        layout.addWidget(title1, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

        save = top_scores[0][1]
        movie1 = QLabel(save.title)
        movie1.setFont(QFont("Courier New", 15, QFont.Weight.Bold))
        movie1.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1, 3, 0, 1, 3, Qt.AlignmentFlag.AlignVCenter)
        movie1_director = QLabel('Director: ' + save.director)
        movie1_director.setFont(QFont("Courier New", 12))
        movie1_director.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_director, 4, 0, 1, 3)
        movie1_runtim = QLabel('RunTime: ' + str(save.runtime) + ' min')
        movie1_runtim.setFont(QFont("Courier New", 12))
        movie1_runtim.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_runtim, 5, 0, 1, 3)
        movie1_lang = QLabel('Language: ' + save.lang)
        movie1_lang.setFont(QFont("Courier New", 12))
        movie1_lang.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_lang, 6, 0, 1, 3)
        movie1_release = QLabel('Release Date: ' + save.release_date)
        movie1_release.setFont(QFont("Courier New", 12))
        movie1_release.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_release, 7, 0, 1, 3)
        button1 = QPushButton("Select")
        button1.setFont(QFont("Courier New", 12))
        button1.setStyleSheet("background-color: #347c99; color: #FFFFFF;")
        button1.clicked.connect(self.screenselect1)
        layout.addWidget(button1, 8, 0)

        save = top_scores[1][1]
        movie1 = QLabel(save.title)
        movie1.setFont(QFont("Courier New", 15, QFont.Weight.Bold))
        movie1.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1, 3, 1, 1, 3, Qt.AlignmentFlag.AlignVCenter)
        movie1_director = QLabel('Director: ' + save.director)
        movie1_director.setFont(QFont("Courier New", 12))
        movie1_director.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_director, 4, 1, 1, 3)
        movie1_runtim = QLabel('RunTime: ' + str(save.runtime) + ' min')
        movie1_runtim.setFont(QFont("Courier New", 12))
        movie1_runtim.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_runtim, 5, 1, 1, 3)
        movie1_lang = QLabel('Language: ' + save.lang)
        movie1_lang.setFont(QFont("Courier New", 12))
        movie1_lang.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_lang, 6, 1, 1, 3)
        movie1_release = QLabel('Release Date: ' + save.release_date)
        movie1_release.setFont(QFont("Courier New", 12))
        movie1_release.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_release, 7, 1, 1, 3)
        button1 = QPushButton("Select")
        button1.setFont(QFont("Courier New", 12))
        button1.setStyleSheet("background-color: #347c99; color: #FFFFFF;")
        button1.clicked.connect(self.screenselect2)
        layout.addWidget(button1, 8, 1)

        save = top_scores[2][1]
        movie1 = QLabel(save.title)
        movie1.setFont(QFont("Courier New", 15, QFont.Weight.Bold))
        movie1.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1, 3, 2, 1, 3, Qt.AlignmentFlag.AlignVCenter)
        movie1_director = QLabel('Director: ' + save.director)
        movie1_director.setFont(QFont("Courier New", 12))
        movie1_director.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_director, 4, 2, 1, 3)
        movie1_runtim = QLabel('RunTime: ' + str(save.runtime) + ' min')
        movie1_runtim.setFont(QFont("Courier New", 12))
        movie1_runtim.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_runtim, 5, 2, 1, 3)
        movie1_lang = QLabel('Language: ' + save.lang)
        movie1_lang.setFont(QFont("Courier New", 12))
        movie1_lang.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_lang, 6, 2, 1, 3)
        movie1_release = QLabel('Release Date: ' + save.release_date)
        movie1_release.setFont(QFont("Courier New", 12))
        movie1_release.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_release, 7, 2, 1, 3)
        button1 = QPushButton("Select")
        button1.setFont(QFont("Courier New", 12))
        button1.setStyleSheet("background-color: #347c99; color: #FFFFFF;")
        button1.clicked.connect(self.screenselect3)
        layout.addWidget(button1, 8, 2)

        save = top_scores[3][1]
        movie1 = QLabel(save.title)
        movie1.setFont(QFont("Courier New", 15, QFont.Weight.Bold))
        movie1.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1, 3, 3, 1, 3, Qt.AlignmentFlag.AlignVCenter)
        movie1_director = QLabel('Director: ' + save.director)
        movie1_director.setFont(QFont("Courier New", 12))
        movie1_director.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_director, 4, 3, 1, 3)
        movie1_runtim = QLabel('RunTime: ' + str(save.runtime) + ' min')
        movie1_runtim.setFont(QFont("Courier New", 12))
        movie1_runtim.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_runtim, 5, 3, 1, 3)
        movie1_lang = QLabel('Language: ' + save.lang)
        movie1_lang.setFont(QFont("Courier New", 12))
        movie1_lang.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_lang, 6, 3, 1, 3)
        movie1_release = QLabel('Release Date: ' + save.release_date)
        movie1_release.setFont(QFont("Courier New", 12))
        movie1_release.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_release, 7, 3, 1, 3)
        button1 = QPushButton("Select")
        button1.setFont(QFont("Courier New", 12))
        button1.setStyleSheet("background-color: #347c99; color: #FFFFFF;")
        button1.clicked.connect(self.screenselect4)
        layout.addWidget(button1, 8, 3, 1, 2)

        save = top_scores[4][1]
        movie1 = QLabel(save.title)
        movie1.setFont(QFont("Courier New", 15, QFont.Weight.Bold))
        movie1.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1, 3, 5, 1, 3, Qt.AlignmentFlag.AlignVCenter)
        movie1_director = QLabel('Director: ' + save.director)
        movie1_director.setFont(QFont("Courier New", 12))
        movie1_director.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_director, 4, 5, 1, 3)
        movie1_runtim = QLabel('RunTime: ' + str(save.runtime) + ' min')
        movie1_runtim.setFont(QFont("Courier New", 12))
        movie1_runtim.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_runtim, 5, 5, 1, 3)
        movie1_lang = QLabel('Language: ' + save.lang)
        movie1_lang.setFont(QFont("Courier New", 12))
        movie1_lang.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_lang, 6, 5, 1, 3)
        movie1_release = QLabel('Release Date: ' + save.release_date)
        movie1_release.setFont(QFont("Courier New", 12))
        movie1_release.setStyleSheet("color: #347c99;")
        layout.addWidget(movie1_release, 7, 5, 1, 3)
        button1 = QPushButton("Select")
        button1.setFont(QFont("Courier New", 12))
        button1.setStyleSheet("background-color: #347c99; color: #FFFFFF;")
        button1.clicked.connect(self.screenselect5)
        layout.addWidget(button1, 8, 5, 1, 2)

        button2 = QPushButton("Back")
        button2.setFont(QFont("Courier New", 12))
        button2.setStyleSheet("background-color: #347c99; color: #FFFFFF;")
        button2.clicked.connect(self.back)
        layout.addWidget(button2, 9, 2, 1, 1)

        info = QLabel('Please FullScreen.')
        info.setFont(QFont("Courier New", 12))
        info.setStyleSheet("color: #347c99;")
        layout.addWidget(info, 10, 0)

        ethical = QLabel("Ethical concerns:")
        ethical.setFont(QFont("Courier New", 10))
        ethical.setStyleSheet("color: #347c99;")
        layout.addWidget(ethical, 11, 0)

        ethical = QLabel("Email - aastha.sharma@mail.utoronto.ca")
        ethical.setFont(QFont("Courier New", 8))
        ethical.setStyleSheet("color: #347c99;")
        layout.addWidget(ethical, 12, 0)

    def screenselect1(self):
        """
        Select the first movie and add it to graph neighbours,
        then return back to the preferences screen.
        """
        if self.w is None:
            main_functions.user_movie_neighbours(self.movie_lst[0][1], self.movie_lst[0][1].item,
                                                 self.graph, self.user_obj.item)
            self.w = PrefenceScreen(self.graph, self.user_obj)
        self.w.show()
        self.close()

    def screenselect2(self):
        """
        Select the first movie and add it to graph neighbours,
        then return back to the preferences screen.
        """
        if self.w is None:
            main_functions.user_movie_neighbours(self.movie_lst[1][1], self.movie_lst[1][1].item,
                                                 self.graph, self.user_obj.item)
            self.w = PrefenceScreen(self.graph, self.user_obj)
        self.w.show()
        self.close()

    def screenselect3(self):
        """
        Select the first movie and add it to graph neighbours,
        then return back to the preferences screen.
        """
        if self.w is None:
            main_functions.user_movie_neighbours(self.movie_lst[2][1], self.movie_lst[2][1].item,
                                                 self.graph, self.user_obj.item)
            self.w = PrefenceScreen(self.graph, self.user_obj)
        self.w.show()
        self.close()

    def screenselect4(self):
        """
        Select the first movie and add it to graph neighbours,
        then return back to the preferences screen.
        """
        if self.w is None:
            main_functions.user_movie_neighbours(self.movie_lst[3][1], self.movie_lst[3][1].item,
                                                 self.graph, self.user_obj.item)
            self.w = PrefenceScreen(self.graph, self.user_obj)
        self.w.show()
        self.close()

    def screenselect5(self):
        """
        Select the first movie and add it to graph neighbours,
        then return back to the preferences screen.
        """
        if self.w is None:
            main_functions.user_movie_neighbours(self.movie_lst[4][1], self.movie_lst[4][1].item,
                                                 self.graph, self.user_obj.item)
            self.w = PrefenceScreen(self.graph, self.user_obj)
        self.w.show()
        self.close()

    def back(self):
        """
        Without selecting a movie return to the preferences screen.
        """
        if self.w is None:
            self.w = PrefenceScreen(self.graph, self.user_obj)
        self.w.show()
        self.close()


class PrefenceScreen(QWidget):
    """The second screen the user sees, also where they put in their preferences and
    the button - Recommendations is clicked to go to next screen
    If the Logout button is clicked then the system goes back to the LogInScreen page.
    """

    def __init__(self, graph: Graph, user_obj: _User) -> None:

        super().__init__()
        self.user_obj = user_obj
        self.graph = graph
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

        genre = QLabel("Genre (ex: Action, Romance, etc):")
        genre.setFont(QFont("Courier New", 15))
        genre.setStyleSheet("color: #347c99;")
        layout.addWidget(genre, 3, 0)
        lang = QLabel("Language (ex: en, hi, fr, etc):")
        lang.setFont(QFont("Courier New", 15))
        lang.setStyleSheet("color: #347c99;")
        layout.addWidget(lang, 4, 0)
        key = QLabel("Keywords (ex: future, love, etc)(max 3):")
        key.setFont(QFont("Courier New", 15))
        key.setStyleSheet("color: #347c99;")
        layout.addWidget(key, 5, 0)
        director = QLabel("Optional: Director (ex: James Cameron):")
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
            self.w = LogInScreen(self.graph)
        self.w.show()
        self.close()

    def recommendation_button(self):
        """
        Function activated when button2 clicked, takes to the Recommendation screen.
        """

        if self.w is None:
            keywords = set()
            if self.key_input1.displayText() != '':
                keywords.add(self.key_input1.displayText())
            if self.key_input2.displayText() != '':
                keywords.add(self.key_input2.displayText())
            if self.key_input3.displayText() != '':
                keywords.add(self.key_input3.displayText())

            self.user_obj.modify_preferences(self.genre_input.displayText(), self.lang_input.displayText(), keywords,
                                             self.director_input.displayText())
            top_scores = main_functions.compute(self.graph, self.user_obj.item)
            self.w = RecommendationScreen(top_scores, self.graph, self.user_obj)
        self.w.show()
        self.close()


class LogInScreen(QWidget):
    """The Log in window that the user sees once the movies are all loaded up in the graph.
    The user can sign up or sign in. When the cross on top is pressed the code stops running and stops.
    Input is only the username, possible buttons are sign up or sign in.
    """

    def __init__(self, graph: Graph) -> None:

        super().__init__()
        self.graph = graph  # loaded graph
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
        if self.input1.displayText() in self.graph.retrieve_vertex_dict():
            user_obj = self.graph.retrieve_item_obj(self.input1.displayText())
            print('Sign in successful!')
            if self.w is None:
                self.w = PrefenceScreen(self.graph, user_obj)
            self.w.show()
            self.close()
        else:
            print('Sign in unsuccessful, please sign up!')

    def sign_up(self):
        """
        if self.input1 in #graph._vertices:
            print('Invalid Username')
        else:
            # call function and move to next screen - preferences
        """
        if self.input1.displayText() in self.graph.retrieve_vertex_dict():
            print("Username already exists! Please sign in.")
        else:
            print('Sign up successful!')
            self.graph.add_user_vertex(self.input1.displayText())
            user_obj = self.graph.retrieve_item_obj(self.input1.displayText())
            if self.w is None:
                self.w = PrefenceScreen(self.graph, user_obj)
            self.w.show()
            self.close()
