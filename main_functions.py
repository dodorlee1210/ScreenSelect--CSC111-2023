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

from python_ta.contracts import check_contracts
from classes import Graph, _Movie


def user_log_in(graph: Graph) -> str:
    """
    Return the username of the user after verifying it exists.
    Add the user to the given graph if non-existent in the graph.
    Reassign user preferences.
    """
    username = input("Please enter your username")

    while username == '':
        print("The username must not be an empty string. Please enter a valid username.")
        username = input("Please enter your username.")

    if graph.verify_vertex(username):
        _user_choices(graph, username)
        return username
    else:
        graph.add_user_vertex(username)
        _user_choices(graph, username)
        return username


def _user_choices(graph: Graph, username: str) -> None:
    """
    Retrieve user movie preference inputs and reassign the given user's preference attributes.

    Precondition:
        - username != ''
    """
    genre = input("Please enter 1 preferred movie genre.")

    lang = input("Please enter 1 preferred language.")

    keywords = input("Please enter a maximum of 3 keywords with spaces in between each keyword.").split()

    while len(keywords) > 3:
        print("Your input should not exceed 3 words.")
        keywords = input("Please enter up to 3 keywords.").split()

    director = input("Please enter 1 preferred movie director's name. Example: FirstName LastName.").split()

    while len(director) != 2:
        print("Please enter the name accordingly: FirstName LastName. There should be a space between the name.")
        director = input("Please enter 1 preferred movie director's name. EX: FirstName LastName.").split()
    user_obj = graph.retrieve_vertex_dict()[username]
    user_obj.modify_preferences(genre, lang, set(keywords), director[0] + ' ' + director[1])


def compute(graph: Graph, username: str) -> dict[int, _Movie]:
    """
    Returns the top 5 movies that will be recommended for a user.
    Preconditions:
        - username != ''
        - graph.retrieve_vertex_dict() != {}
    """
    user_vertex = graph.retrieve_item_obj(username)
    for item in graph.retrieve_vertex_dict():
        if isinstance(item, int) and graph.retrieve_vertex_dict()[item] not in user_vertex.neighbours:
            graph.retrieve_vertex_dict()[item].score(user_vertex, username)

    return user_vertex.retrieve_top_scores()


def user_movie_neighbours(top_movies: dict[int, _Movie], graph: Graph, username: str) -> None:
    """
    Allows the user to choose the movie from top_movies
    Preconditions:
        - len(top_movies) == 5
    """
    user_vertex = graph.retrieve_item_obj(username)
    choice = input("What movie would you like to choose from the recommendations")  # title
    chk = False
    movie_obj = None
    while True:
        for i in top_movies:
            if choice == top_movies[i].title:
                movie_obj = top_movies[i]
                chk = True
                break
        if chk:
            break
        choice = input("Please enter valid movie title from recommendations only.")

    if len(user_vertex.past_10_neighbours) < 10:
        user_vertex.past_10_neighbours.append(movie_obj)  # adding most recent movies watched to the end of the list
        user_vertex.neighbours.add(movie_obj)
        movie_obj.neighbours[user_vertex.item] = user_vertex
    else:
        user_vertex.past_10_neighbours.pop(0)  # removing older movies from the front
        user_vertex.past_10_neighbours.append(movie_obj)
        user_vertex.neighbours.add(movie_obj)
        movie_obj.neighbours[user_vertex.item] = user_vertex


def read_csv_and_create_data(graph: Graph, csv_file1: str, csv_file2: str) -> None:
    """Read the csv filer and add the movies in the greaph class, with the attributes of the different Graph class.
    csv_file1 is the file with information about the Movie without the director
    csv_file2 is the file with the director
    Preconditions:
    - csv_file1 != ''
    - csv_file1 is a valid csv file in the specific format described in proposal
    """
    with open(csv_file1) as csv_file:
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
    """Return a list of the genre/keywords given a string in the format of
    "[{'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}]"
    The returned output is ['Action', 'Adventure', 'Fantasy']
    """
    string = stri.strip("[]")
    dict_list = string.split(", ")
    dict_list1 = [d.strip("{}").split(": ") for d in dict_list]
    dict_list2 = [{k.strip("'"): v.strip("'")} for k, v in dict_list1]
    names_list = {d['"name"'] for d in dict_list2 if '"name"' in d}
    names_list2 = {word.strip('"') for word in names_list}
    return names_list2


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
