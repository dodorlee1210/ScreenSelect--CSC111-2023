"""CSC111 Winter 2023 Final Project: ScreenSelect
===============================
This file contains the classes representing the screens that will be displayed as part of the Graphical User Interface
(GUI)
Copyright and Usage Information
===============================
This file is provided solely for the use of marking the project to the
staff of CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.
This file is Copyright (c) 2023 Aastha Sharma, Sidharth Sawhney,
Narges Movahedian Nezhad, and Dogyu Lee.
"""
from __future__ import annotations
from typing import Optional
from PyQt6.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QGridLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
# from python_ta.contracts import check_contracts
from classes import Graph, _User, _Movie
import main_functions


# @check_contracts
class RecommendationScreen(QWidget):
    """A widget that is displayed as the final step of the movie recommendation process.
    Displays a recommendation page with five top scoring movies for the user to choose from.

    Instance Attributes:
      - graph: The loaded graph.
      - user_obj: The current user for which the Recommendation Screen is open.
      - movie_lst: The top 5 movies to be recommended.
      - w: A variable that will be used to open the Prefence Screen after back button is pressed or if movie has been\
      selected.

    Representation Invariants:
        - len(self.movie_lst) == 5
        - self.graph.retrieve_vertex_dict() != {}
        - self.w is None or isinstance(self.w, PrefenceScreen)
        - isinstance(self.user_obj.item, str) and self.user_obj.item != ''
    """
    graph: Graph
    user_obj: _User
    movie_lst: list[tuple[int, _Movie]]
    w: Optional[PrefenceScreen]

    def __init__(self, top_scores: list[tuple[int, _Movie]], graph: Graph, user_obj: _User) -> None:
        """Initialize this widget with the given top_scores movie list, graph, and user.

        Preconditions:
            - len(top_scores) == 5
            - graph.retrieve_vertex_dict() != {}
            - isinstance(user_obj.item, str) and user_obj.item != ''
        """
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

        # info = QLabel('Please FullScreen.')
        # info.setFont(QFont("Courier New", 12))
        # info.setStyleSheet("color: #347c99;")
        # layout.addWidget(info, 10, 0)

        ethical = QLabel("Ethical concerns:")
        ethical.setFont(QFont("Courier New", 10))
        ethical.setStyleSheet("color: #347c99;")
        layout.addWidget(ethical, 11, 0)

        ethical = QLabel("Email - aastha.sharma@mail.utoronto.ca")
        ethical.setFont(QFont("Courier New", 8))
        ethical.setStyleSheet("color: #347c99;")
        layout.addWidget(ethical, 12, 0)

    def screenselect1(self) -> None:
        """
        Add the first movie of this widget's movie_lst to the neighbours of the graph attribute of this widget.
        Return to PrefenceScreen.
        """
        if self.w is None:
            main_functions.user_movie_neighbours(self.movie_lst[0][1], self.movie_lst[0][1].item,
                                                 self.graph, self.user_obj.item)
            self.w = PrefenceScreen(self.graph, self.user_obj)
        self.w.show()
        self.close()

    def screenselect2(self) -> None:
        """
        Add the second movie of this widget's movie_lst to the neighbours of the graph attribute of this widget.
        Return to PrefenceScreen
        """
        if self.w is None:
            main_functions.user_movie_neighbours(self.movie_lst[1][1], self.movie_lst[1][1].item,
                                                 self.graph, self.user_obj.item)
            self.w = PrefenceScreen(self.graph, self.user_obj)
        self.w.show()
        self.close()

    def screenselect3(self) -> None:
        """
        Add the third movie of this widget's movie_lst to the neighbours of the graph attribute of this widget.
        Return to PrefenceScreen
        """
        if self.w is None:
            main_functions.user_movie_neighbours(self.movie_lst[2][1], self.movie_lst[2][1].item,
                                                 self.graph, self.user_obj.item)
            self.w = PrefenceScreen(self.graph, self.user_obj)
        self.w.show()
        self.close()

    def screenselect4(self) -> None:
        """
        Add the fourth movie of this widget's movie_lst to the neighbours of the graph attribute of this widget.
        Return to PrefenceScreen
        """
        if self.w is None:
            main_functions.user_movie_neighbours(self.movie_lst[3][1], self.movie_lst[3][1].item,
                                                 self.graph, self.user_obj.item)
            self.w = PrefenceScreen(self.graph, self.user_obj)
        self.w.show()
        self.close()

    def screenselect5(self) -> None:
        """
        Add the fifth movie of this widget's movie_lst to the neighbours of the graph attribute of this widget.
        Return to PrefenceScreen
        """
        if self.w is None:
            main_functions.user_movie_neighbours(self.movie_lst[4][1], self.movie_lst[4][1].item,
                                                 self.graph, self.user_obj.item)
            self.w = PrefenceScreen(self.graph, self.user_obj)
        self.w.show()
        self.close()

    def back(self) -> None:
        """
        Return to PrefenceScreen.
        """
        if self.w is None:
            self.w = PrefenceScreen(self.graph, self.user_obj)
        self.w.show()
        self.close()


# @check_contracts
class PrefenceScreen(QWidget):
    """A widget that is displayed as the second step of the movie recommendation process.
    Displays a preference input page with many movie categories for the user to fill out.

    Instance Attributes:
      - graph: The loaded graph.
      - user_obj: The current user for which the Recommendation Screen is open.
      - genre_input: Stores the genre inputted by the user
      - lang_input: Stores the language inputted by the user
      - key_input1: Stores the first keyword inputted by the user
      - key_input2: Stores the second keyword inputted by the user
      - key_input3: Stores the third keyword inputted by the user
      - director_input: Stores the director name inputted by the user
      - w: A variable that will be used to open the LogIn screen if the logout button is pressed or Recommendation\
       Screen is the recommend button is pressed.

    Representation Invariants:
        - self.graph.retrieve_vertex_dict() != {}
        - self.w is None or isinstance(self.w, RecommendationScreen) or isinstance(self.w, LogInScreen)
        - isinstance(self.user_obj.item, str) and self.user_obj.item != ''
        - isinstance(self.key_input1, QLineEdit())
        - isinstance(self.key_input2, QLineEdit())
        - isinstance(self.key_input3, QLineEdit())
        - isinstance(self.genre_input, QLineEdit())
        - isinstance(self.director_input, QLineEdit())
    """
    graph: Graph
    user_obj: _User
    genre_input: QLineEdit
    lang_input: QLineEdit
    key_input1: QLineEdit
    key_input2: QLineEdit
    key_input3: QLineEdit
    director_input: QLineEdit
    w: Optional[RecommendationScreen | LogInScreen]

    def __init__(self, graph: Graph, user_obj: _User) -> None:
        """Initialize this widget with the given graph and user.
        Preconditions:
            - graph.retrieve_vertex_dict() != {}
            - isinstance(user_obj.item, str) and user_obj.item != ''
             """
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

    def log_out(self) -> None:
        """
        Return to LogInScreen.
        """
        if self.w is None:
            self.w = LogInScreen(self.graph)
        self.w.show()
        self.close()

    def recommendation_button(self) -> None:
        """Update user attributes.
        Obtain top 5 scoring movies list based on user preferences and selection.
        Display RecommendationScreen.
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


# @check_contracts
class LogInScreen(QWidget):
    """A widget that is displayed as the first step of the movie recommendation process.
    Displays a login page where the user can sign in or sign-up.

    Instance Attributes:
      - graph: The loaded graph.
      - input1: Stores the username.
      - w: A variable that will be used to open the Prefence Screen after the user successfully signs in or signs up.

    Representation Invariants:
        - self.graph.retrieve_vertex_dict() != {}
        - self.w is None or isinstance(self.w, PrefenceScreen)
        - isinstance(self.input1, QLineEdit())
    """
    graph: Graph
    input1: QLineEdit
    w: Optional[PrefenceScreen]

    def __init__(self, graph: Graph) -> None:
        """Initialize this widget with the given graph.
        Precondition:
            - graph.retrieve_vertex_dict() != {}
             """

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

    def sign_in(self) -> None:
        """
        Verify whether the user exists in the graph attribute and display PreferenceScreen.

        If the user does not exist in the graph attribute, print to try signing up first.
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

    def sign_up(self) -> None:
        """
        Add a new user vertex to this widget's graph attribute and display PreferenceScreen.

        If the input username already exists in the graph attribute, print to try signing in.
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


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['E9992', 'E9997', 'E9998', 'R0902', 'R0915', 'E0611'],
        'extra-imports': ['PyQt6.QtWidgets', 'PyQt6.QtCore', 'PyQt6.QtGui', 'classes', 'main_functions'],
        'allowed-io': ['LogInScreen.sing_in', 'LogInScreen.sing_up'],

    })
