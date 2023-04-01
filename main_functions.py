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
from python_ta.contracts import check_contracts
from classes import Graph, _Movie, _User


# def user_log_in(graph: Graph) -> str:
#     """
#     Return the username of the user after verifying it exists.
#     Add the user to the given graph if non-existent in the graph.
#     Reassign user preferences.
#     """
#     username = input("Please enter your username")
#
#     while username == '':
#         print("The username must not be an empty string. Please enter a valid username.")
#         username = input("Please enter your username.")
#
#     if graph.verify_vertex(username):
#         _user_choices(graph, username)
#         return username
#     else:
#         graph.add_user_vertex(username)
#         _user_choices(graph, username)
#         return username


# def user_choices(graph: Graph, username: str) -> None:
#     """
#     Retrieve user movie preference inputs and reassign the given user's preference attributes.
#
#     Precondition:
#         - username != ''
#     """
#     genre = input("Please enter 1 preferred movie genre.")
#
#     lang = input("Please enter 1 preferred language.")
#
#     keywords = input("Please enter a maximum of 3 keywords with spaces in between each keyword.").split()
#
#     while len(keywords) > 3:
#         print("Your input should not exceed 3 words.")
#         keywords = input("Please enter up to 3 keywords.").split()
#
#     director = input("Please enter 1 preferred movie director's name. Example: FirstName LastName.").split()
#
#     while len(director) != 2:
#         print("Please enter the name accordingly: FirstName LastName. There should be a space between the name.")
#         director = input("Please enter 1 preferred movie director's name. EX: FirstName LastName.").split()
#     user_obj = graph.retrieve_vertex_dict()[username]
#     user_obj.modify_preferences(genre, lang, set(keywords), director[0] + ' ' + director[1])
#

def compute(graph: Graph, username: str) -> list[tuple[int, _Movie]]:
    """
    Returns the top 5 movies that will be recommended for a user.
    Preconditions:
        - username != ''
        - graph.retrieve_vertex_dict() != {}
    """
    user_vertex = graph.retrieve_item_obj(username)
    for item in graph.retrieve_vertex_dict():
        if isinstance(item, int):
            chk = True
            for movie_obj in user_vertex.neighbours:
                if graph.retrieve_vertex_dict()[item] is movie_obj:
                    chk = False
                    break
            if not chk:
                continue
            graph.retrieve_vertex_dict()[item].score(user_vertex, username)

    return user_vertex.retrieve_top_scores()


def user_movie_neighbours(chosen_movie: _Movie, graph: Graph, username: str) -> None:
    """
    Record the changes given the movie chosen for the user.
    """
    user_vertex = graph.retrieve_item_obj(username)

    if len(user_vertex.past_10_neighbours) < 10:
        user_vertex.past_10_neighbours.append(chosen_movie)  # adding most recent movies watched to the end of the list
        user_vertex.neighbours.add(chosen_movie)
        chosen_movie.neighbours[user_vertex.item] = user_vertex
    else:
        user_vertex.past_10_neighbours.pop(0)  # removing older movies from the front
        user_vertex.past_10_neighbours.append(chosen_movie)
        user_vertex.neighbours.add(chosen_movie)
        chosen_movie.neighbours[user_vertex.item] = user_vertex


def read_csv_and_create_data(graph: Graph, csv_file1: str, csv_file2: str) -> None:
    """Read the csv filer and add the movies in the greaph class, with the attributes of the different Graph class.
    csv_file1 is the file with information about the Movie without the director
    csv_file2 is the file with the director
    Preconditions:
    - csv_file1 != ''
    - csv_file1 is a valid csv file in the specific format described in proposal
    """
    with open(csv_file1, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            # if row[1] == '[]' or row[4] == '[]':
            #     continue
            print(row)
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
    """Return a list of the genre/keywords given a string in the format of
    "[{'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}]"
    The returned output is ['Action', 'Adventure', 'Fantasy']
    """
    string = stri.strip("[]")
    list_of_dicts = ast.literal_eval('[' + string + ']')
    set_so_far = set()
    for dict_1 in list_of_dicts:
        set_so_far.add(dict_1['name'])
    return set_so_far


def _find_director(csv_file2: str, movie_name: str) -> Any:
    """
    Return the director of the movie if found in the csv_file2 based on the movie name given.
    The return value is none if no director found in the movie dataset
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
