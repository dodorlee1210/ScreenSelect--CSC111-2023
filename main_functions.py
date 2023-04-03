"""CSC111 Winter 2023 Final Project: ScreenSelect
===============================
This module contains a collection of top level functions that will be caled by the main.py.
Copyright and Usage Information
===============================
This file is provided solely for the use of marking the project to the
staff of CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.
This file is Copyright (c) 2023 Aastha Sharma, Sidharth Sawhney,
Narges Movahedian Nezhad, and Dogyu Lee.
"""
import csv
from typing import Any
import ast
from classes import Graph, _Movie


def compute(graph: Graph, username: str) -> list[tuple[int, _Movie]]:
    """
    Return a list of the top 5 movies that will be recommended for a user.
    Preconditions:
        - username != ''
        - graph.retrieve_vertex_dict() != {}
    """
    user_vertex = graph.retrieve_item_obj(username)
    for item in graph.retrieve_vertex_dict():
        if isinstance(item, int):
            chk = True
            for id_movie in user_vertex.neighbours:
                if graph.retrieve_vertex_dict()[item] is user_vertex.neighbours[id_movie]:
                    chk = False
                    break
            if not chk:
                continue
            graph.retrieve_vertex_dict()[item].score(user_vertex, username)

    return user_vertex.retrieve_top_scores()


def user_movie_neighbours(chosen_movie: _Movie, id_move: int, graph: Graph, username: str) -> None:
    """
    Map the chosen_movie to user's neighbours and update user's past_10_neighbours with it.
    """
    user_vertex = graph.retrieve_item_obj(username)

    if len(user_vertex.past_10_neighbours) < 10:
        user_vertex.past_10_neighbours.append(chosen_movie)  # adding most recent movies watched to the end of the list
        user_vertex.neighbours[id_move] = chosen_movie
        chosen_movie.neighbours[user_vertex.item] = user_vertex
    else:
        user_vertex.past_10_neighbours.pop(0)  # removing older movies from the front
        user_vertex.past_10_neighbours.append(chosen_movie)
        user_vertex.neighbours[id_move] = chosen_movie
        chosen_movie.neighbours[user_vertex.item] = user_vertex


def read_csv_and_create_data(graph: Graph, csv_file1: str, csv_file2: str) -> None:
    """Read the csv files and add the movies as vertices, after updating each vertex with relevant data, in the given graph.
    Preconditions:
    - csv_file1 != ''
    - csv_file1 is a valid csv file in the specific format described in proposal
    """
    with open(csv_file1, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            id_item = int(row[3])
            genre = _find_genre_keyword_list(row[1])
            lan = row[5]
            keyword = _find_genre_keyword_list(row[4])
            title = row[17]
            director = _find_director(csv_file2, title)
            vote_average = float(row[18])
            overview = row[7]
            runtime = int(row[13])
            realese_date = row[11]
            graph.add_movie_vertex(item=id_item, genre=genre, lang=lan, keyword=keyword, director=director,
                                   title=title, vote_avg=vote_average, overview=overview, runtime=runtime,
                                   release_date=realese_date)


def _find_genre_keyword_list(stri: str) -> set[str]:
    """Return a set of the genre or keywords given a string in the format of dictionaries that contain strings and ints within a list.
    """
    string = stri.strip("[]")
    list_of_dicts = ast.literal_eval('[' + string + ']')
    set_so_far = set()
    for dict_1 in list_of_dicts:
        set_so_far.add(dict_1['name'])
    return set_so_far


def _find_director(csv_file2: str, movie_name: str) -> Any:
    """
    Return the director of the movie by the given movie_name.
    If no director is found, return None.
    Precondition:
    - movie_name != ''
    - csv_file2 != ''
    """
    with open(csv_file2) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            if movie_name == row[1]:
                string = row[3]
                credit_eval = eval(string)
                director = next((cre["name"] for cre in credit_eval if cre["job"] == "Director"), None)
                if isinstance(director, str):
                    return director
                else:
                    return None


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
