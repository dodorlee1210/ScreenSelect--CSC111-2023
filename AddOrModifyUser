"""CSC111 Winter 2023 Final Project: ScreenSelect

===============================
This module contains a collection of Python classes and functions that
would be used to make our system. Classes include Graph,
_Vertex (abstract class), _Movie and _User (subclasses of _Vertex).
Please read before editing the file and comment the changes you make.

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
from dataclasses import dataclass
from vertex_main import Graph


def user_log_in(graph: Graph) -> str:
    """
    If user doesn't exist, add user to the given graph with its movie preferences recorded.
    If user exists, modify its movie preferences.
    """
    username = input("Please enter your username")

    while username == '':
        print("The username must not be an empty string. Please enter a valid username.")
        username = input("Please enter your username.")

    if graph.verify_vertex(username):
        _user_choices(graph, username)
        return username
    else:
        graph.add_vertex(username)
        _user_choices(graph, username)
        return username


def _user_choices(graph: Graph, username: str) -> None:
    """
    Retrieve user movie preferences and store them for the user.

    Precondition:
    - username != ''
    """
    genre = input("Please enter 1 preferred movie genre.")

    lang = input("Please enter 1 preferred language.")

    keywords = input("Please enter a maximum of 3 keywords with spaces in between each keyword.").split()

    while len(keywords) > 3:
        print("Your input should not exceed 3 words.")
        keywords = input("Please enter up to 3 keywords.").split()

    director = input("Please enter 1 preferred movie director's name. EX: FirstName LastName.").split()

    while len(director) != 2:
        print("Please enter the name accordingly: FirstName LastName. There should be a space between the name.")
        director = input("Please enter 1 preferred movie director's name. EX: FirstName LastName.")

    graph.modify_preferences(username, genre, lang, set(keywords), director[0] + ' ' + director[1])


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the
    # following lines. (In PyCharm, select the lines below and press Ctrl/Cmd
    # + / to toggle comments.) You can use "Run file in Python Console" to run
    # PythonTA, and then also test your methods manually in the console.
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['E9992', 'E9997']
    })
