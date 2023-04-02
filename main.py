"""CSC111 Winter 2023 Final Project: ScreenSelect
===============================
This module is the main file that will be run when executing the program.
Copyright and Usage Information
===============================
This file is provided solely for the use of marking the project to the
staff of CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.
This file is Copyright (c) 2023 Aastha Sharma, Sidharth Sawhney,
Narges Movahedian Nezhad, and Dogyu Lee.
"""
from classes import Graph
import main_functions
from screen_select_gui import LogInScreen
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    graph = Graph()
    main_functions.read_csv_and_create_data(graph, 'data/tmdb_5000_movies1.csv', 'data/tmdb_5000_credits.csv')
    app = QApplication(sys.argv)
    window = LogInScreen(graph)
    window.show()  # To show the gui window the above code is very static to a window open
    sys.exit(app.exec())
