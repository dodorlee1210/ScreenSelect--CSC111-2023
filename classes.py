"""
This class contains the classes that would be used to make our system.
Classes include Graph, _Vertex (abstract class), _Movie and _User
(subclasses of _Vertex)
"""
from python_ta.contracts import check_contracts
from typing import Optional


@check_contracts
class Graph:
    """
    A graph.
    """
    # Private Instance Attributes:
    # - _vertices: A collection of the vertices contained in this
    # graph. Maps item to a Movie or _User instance.
    _vertices: dict[int | str, _Vertex]

    # It would be str if the value is a User and int if the value is Movie.

    def __init__(self) -> None:
        """
        Initialize an empty graph (no vertices or edges).
        """
        self._vertices = {}


@check_contracts
class _Vertex:
    """
    A vertex in a graph.

    Instance Attributes:
      - item: The data stored in this vertex.
      - genre: A movie genre.
      # more than one genre exists for many movies in dataset?
      - lang: The language used in a movie.
      - keywords: The collection of keywords used to describe a movie.
      - director: The director of a movie.

    Representation Invariant:
      - self.item != ''
      - self.genre != ''
      - self.lang != ''
      - self.keywords is None or len(self.keywords) >= 1
      - self.director is None or self.director != ''
    """
    item: int | str
    genre: str
    lang: str
    keywords: Optional[set[str]]
    director: Optional[str]


@check_contracts
class _Movie(_Vertex):
    """
    A vertex that represents a movie in Graph.

    Instance Attributes:
      - title: The title of this movie.
      - vote_average: The average rating of this movie.
      - overview: A brief overview of this movie.
      - runtime: The runtime of this movie.
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
    # _total_score: The score that represents how much this movie
    # matches the user's preferences.
    title: str
    vote_average: float
    overview: str
    runtime: int
    release_date: str
    neighbours: dict[str, _User]
    _total_score: int


@check_contracts
class _User(_Vertex):
    """
    A vertex that represents a user in Graph.

    Instance Attributes:
      - neighbours: A collection representing the user's choice of the
      past movie recommendations.
      - past_10_neighbours: A collection representing the user's 10
      most recently selected movies.

    Representation Invariants:
      - len(self.keywords) <= 3
      - len(self.past_10_neighbours) <= 10
      - self not in self.neighbours
      - all(type(u) is not type(self) for u in self.neighbours)
      - all(self in u.neighbours for u in self.neighbours)
      """
    # Private Instance Attributes:
    # _top_scores: The mapping containing the top five scoring MOVIE.
    # RI: all(movie not in self.neighbours and movie not in
    # self.past_10_neighbours for movie in self._top_scores.values())
    neighbours: set[_Movie]
    past_10_neighbours: list[_Movie]
    _top_scores: dict[int, _Movie]


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
