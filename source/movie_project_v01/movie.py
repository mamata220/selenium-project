class Movie:

    def __init__(self, dir, actorname, movie_genre, r_year, moviename):
        self.director = dir
        self.actor = actorname
        self.genre = movie_genre
        self.rel_year = r_year
        self.movie_name = moviename

    """def __repr__(self):
        r_year = str(self.rel_year)
        #print(f"director: {self.director}\n actor :{self.actor} \ngenre : {self.genre} \n rel_year : {r_year}  \nmovie_name : {self.movie_name}") 
        return f"director: {self.director}\nactor : {self.actor} \ngenre : {self.genre} \nrel_year : {str(self.rel_year)} \nmovie_name : {self.movie_name}"
        """

    def __str__(self):
        return f"director: {self.director}\nactor : {self.actor} \ngenre : {self.genre} \nrel_year : {str(self.rel_year)} \nmovie_name : {self.movie_name}"


