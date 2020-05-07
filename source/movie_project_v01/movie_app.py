from source.movie_project_v01.movie import Movie
from source.movie_project_v01.movies_db import MoviesDb

black_panther = Movie("j.ross", "chadwick", "action", 2007, "Black panther")
mdb = MoviesDb()


def input_movie_details_byconsole():
    movie_name = input("Movie Name: ")
    director_name = input("Director Name: ")
    release_year = int(input("Release Year: "))
    genre = input("genre (separated by comma): ")
    actors = input("Actors Names (separated by comma): ")

    movie_by_user = Movie(director_name, actors, genre, release_year, movie_name)
    return movie_by_user


"""for i in range(0, 3):
    mu = input_movie_details_byconsole()
    #mdb.add_movie(black_panther)
    #mdb.add_movie(mu)
    #mdb.show_all_movies(
    mdb.add_movie_to_movies_db_txtfile(mu)
    print()"""
mdb.read_movie_from_movies_db_txtfile()
# Search
#movie_name = input("Which movie details you want see, please enter its name: ")
#search_result = mdb.search_movie_by_title(movie_name)
#print(search_result)

