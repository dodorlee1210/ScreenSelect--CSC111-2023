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
from typing import Optional
from python_ta.contracts import check_contracts
from classes import Graph, _Vertex, _User, _Movie
import main_functions

graph = Graph()
main_functions.read_csv_and_create_data(graph, 'data/tmdb_5000_movies.csv', 'data/tmdb_5000_credits.csv')
ans = 1
while ans:
    username = main_functions.user_log_in(graph)
    top_movies = main_functions.compute(graph, username)
    main_functions.user_movie_neighbours(top_movies, graph, username)
    answer = input("Would you like to watch another movie? Enter 'yes' or 'no'")
    if answer == 'yes':
        ans = 1
    else:
        ans = 0

# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod(verbose=True)
#
#     # When you are ready to check your work with python_ta, uncomment the
#     # following lines. (In PyCharm, select the lines below and press Ctrl/Cmd
#     # + / to toggle comments.) You can use "Run file in Python Console" to run
#     # PythonTA, and then also test your methods manually in the console.
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['E9992', 'E9997']
    })
