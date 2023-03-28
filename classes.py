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


@check_contracts
class _Vertex:
    """
    A vertex in a graph.

    Instance Attributes:
      - item: The username or movie id stored in this vertex.
      - genre: The collection of genre in a movie.
      - lang: The language used in a movie.
      - keywords: The collection of keywords used to describe a movie.
      - director: The director of a movie.

    Representation Invariant:
      - self.item != ''
      - self.genre is None or self.genre != []
      - self.lang is None or self.lang != ''
      - self.keywords is None or len(self.keywords) >= 1
      - self.director is None or self.director != ''
    """
    item: int | str
    genre: Optional[list[str]]
    lang: Optional[str]
    keywords: Optional[set[str]]
    director: Optional[str]

    def __init__(self) -> None:
        """
        Innitialize the empty class that will be rewritten by the _movie/_user class
        """
        self.item = ''
        self.genre = None
        self.lang = None
        self.keywords = None
        self.director = None


@check_contracts
class _Movie(_Vertex):
    """
    A vertex that represents a movie in Graph.

    Instance Attributes:
      - title: The title of this movie.
      - vote_average: The average rating of this movie.
      - overview: A brief overview of this movie.
      - runtime: The runtime of this movie in minutes.
      - release_date: The date this movie was released.
      - neighbours: A mapping containing the neighbours of this vertex.

    Represenatation Invariants:
      - self.title != ''
      - self.vote_average >= 0.0
      - self.overview != ''
      - self.runtime >= 0
      - self.release_date != ''
      - self not in self.neighbours
      - all(type(u) is not type(self) for u in self.neighbours)
      - all(self in u.neighbours for u in self.neighbours)
    """
    # Private Instance Attributes:
    # _total_score: A dictionary that stores users name and score for this movie based on Movie preferences
    title: str
    vote_average: float
    overview: str
    runtime: int
    release_date: str
    neighbours: dict[str, _Vertex]
    _total_score: dict[str, int]

    def __init__(self, item: int, genre: list[str], lang: str, keyword: set[str], director: str, title: str,
                 vote_avg: float, overview: str, runtime: int, release_date: str) -> None:
        """
        Innitialize the vertex given the above attributes of the Movie class (subclass of the Vertex Class).
        """
        super().__init__()
        self.item = item
        self.genre = genre
        self.lang = lang
        self.keywords = keyword
        self.director = director
        self.title = title
        self.vote_average = vote_avg
        self.overview = overview
        self.runtime = runtime
        self.release_date = release_date
        self.neighbours = {}
        self._total_score = {}


@check_contracts
class _User(_Vertex):
    """
    A vertex that represents a user in Graph.

    Instance Attributes:
      - password: The password for the user to enter their account
      - neighbours: A collection representing the user's choice of the past movie choices from
      the recommended options.
      - past_10_neighbours: A collection representing the user's 10 most recently choosen movies
      from the recommended options.

    Representation Invariants:
      - len(self.keywords) <= 3
      - len(self.past_10_neighbours) <= 10
      - self not in self.neighbours
      - all(type(u) is not type(self) for u in self.neighbours)
      - all(self in u.neighbours for u in self.neighbours)
      """
    # Private Instance Attributes:
    # _top_scores: The mapping containing the top five scoring MOVIE.
    # RI: all(mov not in self.neighbours and mov not in self.past_10_neighbours for mov in self._top_scores.values())
    password: str
    neighbours: set[_Vertex]
    past_10_neighbours: list[_Vertex]
    _top_scores: dict[int, _Vertex]

    def __init__(self, name: str, password: str) -> None:
        """
        Innitialize the vertex given the above attributes of the User class (subclass of the Vertex Class).
        """
        super().__init__()
        self.item = name
        self.genre = None
        self.lang = None
        self.keywords = None
        self.director = None
        self.password = password
        self.neighbours = set()
        self.past_10_neighbours = []
        self._top_scores = {}


@check_contracts
class Graph:
    """
    A graph class representing the enitre system.
    """
    # Private Instance Attributes:
    # - _vertices: A collection of the vertices contained in this graph. Maps item to a Movie or _User instance.
    # str - the value is a User and int - the value is Movie.
    _vertices: dict[int | str, _Vertex]

    def __init__(self) -> None:
        """
        Initialize an empty graph (no vertices or edges).
        """
        self._vertices = {}


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
