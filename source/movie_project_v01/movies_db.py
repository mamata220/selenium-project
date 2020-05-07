
class MoviesDb:
    def __init__(self):
        self.mdb = []

    def add_movie(self, m):
        self.mdb.append(m)

    def show_all_movies(self):
        print(f"{len(self.mdb)}  movies stored in db, Below are the details ")
        for m in self.mdb:
            print(m)
            print()

    def search_movie_by_title(self, m_name):
        for m in self.mdb:
            if m.movie_name == m_name:
                return m

    def add_movie_to_movies_db_txtfile(self, mov_obj):
        file1 = open("movies_db.txt.", "w")  # append mode
        file2 = f"{mov_obj.director},{mov_obj.actor},{mov_obj.genre},{(str(mov_obj.rel_year))},{mov_obj.movie_name}"
        file1.write(file2+"\n")

        file1.close()

    def read_movie_from_movies_db_txtfile(self):
        file1 = open("movies_db.txt.", "r")  # read mode
        print(file1.read())

        file1.close()
