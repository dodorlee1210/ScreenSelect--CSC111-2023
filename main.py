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
import pickle

if __name__ == '__main__':
    # Below runs the program with 4803 movies and takes the graph saved in the saved_state file
    with open('data/file.pkl', 'rb') as file:
        # Call load method to deserialze
        graph = pickle.load(file)
    app = QApplication(sys.argv)
    window = LogInScreen(graph)
    window.show()
    sys.exit(app.exec())

    # To check if the graph loads properly, uncomment the bottom code, which creates a new graph and loads 400 movies
    # please comment the above code
    # The call to load 400 movies will take approx 2 mins!
    # Place the data folder in the repository containing the other files, or else change the path depending on where the folder is stored.
    # graph_small = Graph()
    # main_functions.read_csv_and_create_data(graph_small, 'data/tmdb_5000_movies1.csv', 'data/tmdb_5000_credits.csv') 
    # app = QApplication(sys.argv)
    # window = LogInScreen(graph_small)
    # window.show()  # To show the gui window the above code is very static to a window open
    # sys.exit(app.exec())
