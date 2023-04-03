"""CSC111 Winter 2023 Final Project: ScreenSelect
===============================
This module is the saved state that will be used when running main.

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
import pickle

graph = Graph()
main_functions.read_csv_and_create_data(graph, 'data/tmdb_5000_movies.csv', 'data/tmdb_5000_credits.csv')
with open('file.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(graph, file)
