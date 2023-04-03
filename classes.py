"""CSC111 Winter 2023 Final Project: ScreenSelect
===============================
This module contains a collection of Python classes and methods that
would be used to make our system. Classes include Graph,
_Vertex (superclass class of _Movie and _User), _Movie and _User (subclasses of _Vertex).

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
from dataclasses import dataclass
from python_ta.contracts import check_contracts


@check_contracts
@dataclass
class _Vertex:
    """
    A class representing a vertex (movie or user) in a graph.
    Instance Attributes:
      - item: A unique username or movie id.
      - genre: A user's preferred genre or the collection of genres of a movie.
      - lang: The language used in a movie.
      - keywords: The collection of keywords that describe a movie.
      - director: The director of a movie.
    Representation Invariants:
      - self.item != ''
    """
    item: int | str
    genre: Optional[set[str] | str] = None
    lang: Optional[str] = None
    keywords: Optional[set[str]] = None
    director: Optional[str] = None


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
      - neighbours: A mapping of user vertices to their usernames representing the edges between the user vertex and this movie vertex.
    Represenatation Invariants:

      - self.title != ''
      - isinstance(self.item, int)
      - self.genre is None or (isinstance(self.genre, set) and (all(isinstance(s,str) for s in self.genre)))
      - self.lang is None or isinstance(self.lang,str)
      - self.keywords is None or (isinstance(self.keywords, set) and (all(isinstance(s,str) for s in self.keywords)))
      - self.director is None or isinstance(self.director, str)
      - a movie can never be a neighbour of itself
      - self.vote_average >= 0.0
      - self.overview != ''
      - self.runtime >= 0
      - self.release_date != ''
      - self not in self.neighbours
      - all(!isinstance(u,self) for u in self.neighbours)
      - all([[self is self.neighbours[s].neighbours[id] for id self.neighbours[s].neighbours] for s in self.neighbours])
      - all(isinstance(self.neighbours[u], _User) for u in self.neighbours)
    """
    # Private Instance Attributes:
    # _total_score: A dictionary that maps users name to the preference score for this movie.
    title: str
    vote_average: float
    overview: str
    runtime: int
    release_date: str
    neighbours: dict[str, _Vertex]
    _total_score: dict[str, int]

    def __init__(self, item: int, genre: set[str], lang: str, keyword: set[str], director: Optional[str], title: str,
                 vote_avg: float, overview: str, runtime: int, release_date: str) -> None:
        """
        Initialize the vertex given the above attributes of the Movie class (subclass of the Vertex Class).
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

    def score(self, user: _Vertex, username: str) -> None:
        """
        Compute a preference score based on the given user's preferences and selected movies.
        Update this movie's _total_score by mapping the preference score of a user to that user's username.
        Update the given user's _top_scores attribute if it has less than 5 movies or if its preference score is greater than the minimum score of that list.

        Preconditions:
            - username != ''
        """
        score = 0
        if user.genre in self.genre:
            score += 10
        else:
            score += 5

        if user.lang == self.lang:
            score += 10
        else:
            score += 5

        for keyword in user.keywords:
            if keyword in self.keywords:
                score += 5

        if user.director == self.director:
            score += 5

        for movie_obj in user.past_10_neighbours:
            for key in movie_obj.keywords:
                if key in self.keywords:
                    score += 5
            if (movie_obj.director is not None and self.director is not None) and (movie_obj.director == self.director):
                score += 5
            if movie_obj.lang == self.lang:
                score += 10
            else:
                score += 5
            for key in movie_obj.genre:
                if key in self.genre:
                    score += 10
                else:
                    score += 5

        self._total_score[username] = score
        if (len(user.retrieve_top_scores()) == 5) and min(dict(user.retrieve_top_scores())) <= score:
            t = ()
            for tup in user.retrieve_top_scores():
                if tup[0] == min(dict(user.retrieve_top_scores())):
                    t = tup
                    break
            user.retrieve_top_scores().remove(t)
            user.retrieve_top_scores().append((score, self))
        else:
            user.retrieve_top_scores().append((score, self))


@check_contracts
class _User(_Vertex):
    """
    A vertex that represents a user in Graph.
    Instance Attributes:
      - neighbours: A dictionary that maps past user's choices of recommended movies to its id.
      - past_10_neighbours: A list representing the user's 10 most recently selected movies from the recommended options.

    Representation Invariants:
      - self.keywords is None or (0 <= len(self.keywords) <= 3)
      - self.keywords is None or (isinstance(self.keywords, set) and (all(isinstance(s,str) for s in self.keywords)))
      - isinstance(self.item , str)
      - self.lang is None or isinstance(self.lang,str)
      - self.genre is None or isinstance(self.genre, str)
      - len(self.past_10_neighbours) <= 10
      - a user can never be a neighbour of itself
      - all(!isinstance(u,self) for u in self.neighbours)
      - all([[self is self.neighbours[s].neighbours[id] for id self.neighbours[s].neighbours] for s in self.neighbours])
      - all(isinstance(self.neighbours[u], _User) for u in self.neighbours)
      """
    # Private Instance Attributes:
    # _top_scores: The list containing tuples of top five scoring movies with their preference scores. (scores come first, then comes _Movie)
    # Representation Invariant: Movies in self._top_scores should never part of movies previously selected by the user.
    # Representation Invariant: len(self._top_scores) <= 5

    neighbours: dict[int, _Movie]  # int is the id of movie (item)
    past_10_neighbours: list[_Movie]
    _top_scores: list[tuple[int, _Movie]]  # int represents score

    def __init__(self, name: str) -> None:
        """
        Initialize the vertex with the given username.
        """
        super().__init__()
        self.item = name
        self.genre = None
        self.lang = None
        self.keywords = None
        self.director = None
        self.neighbours = {}
        self.past_10_neighbours = []
        self._top_scores = []

    def retrieve_top_scores(self) -> list[tuple[int, _Movie]]:
        """
        Return _top_scores, a list of tuples containing a movie's id and a movie vertex.
        """
        return self._top_scores

    def modify_preferences(self, genre: Optional[str], lang: Optional[str], keywords: Optional[set[str]],
                           director: Optional[str]) -> None:
        """
        Modify the instance attributes of this user given the genre, lang, keywords, and director.
        """
        self.genre = genre
        self.lang = lang
        self.keywords = keywords
        self.director = director


@check_contracts
class Graph:
    """
    A graph class representing the enitre recommendation and selection system.
    """
    # Private Instance Attributes:
    # - _vertices: A collection of the vertices contained in this graph. Maps item to a _Movie (id) or _User (name)
    # instance.

    _vertices: dict[int | str, _Vertex]  # unique names and ids only as keys

    def __init__(self) -> None:
        """
        Initialize an empty graph (no vertices or edges).
        """
        self._vertices = {}

    def add_user_vertex(self, username: str) -> None:
        """
        Add a user to this graph.
        Precondition:
        - username != ''
        - username not in self._vertices
        """
        self._vertices[username] = _User(username)

    def retrieve_item_obj(self, item: str | int) -> _Vertex:
        """
        Return the _User or _Movie instance corresponding to the username or id.
        Precondition:
        - item != ''
        """
        return self._vertices[item]

    def retrieve_vertex_dict(self) -> dict[int | str, _Vertex]:
        """
        Return the _User instance corresponding to the username.
        """
        return self._vertices

    def add_movie_vertex(self, item: int, genre: set[str], lang: str, keyword: set[str], director: Optional[str],
                         title: str,
                         vote_avg: float, overview: str, runtime: int, release_date: str) -> None:
        """Create a movie object and add it into this graph.
        Preconditions:
        - isinstance(item, int)
        - title != ''
        - vote_average >= 0.0
        - overview != ''
        - runtime >= 0
        - release_date != ''
        """
        movie = _Movie(item, genre, lang, keyword, director, title, vote_avg, overview, runtime, release_date)
        self._vertices[item] = movie


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['E9992', 'E9997']
    })
