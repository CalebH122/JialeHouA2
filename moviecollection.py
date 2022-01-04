"""..."""

# TODO: Create your MovieCollection class in this file
from movie import Movie
import csv


class MovieCollection(Movie):
    """..."""

    def __init__(self):
        super().__init__()
        self.movies = []

    def __str__(self):
        if not self.movies:
            return "No movie"
        else:
            for movie in self.movies:
                print(movie)

    def load_movies(self, file):
        with open(file, 'r') as movie_file:
            movies = csv.reader(movie_file)
            for movie in movies:
                if movie[3] == 'w':
                    movie.is_watched = True
                    new_movie = Movie(movie[0], movie[1], movie[2], movie.is_watched)
                    self.movies.append(new_movie)
                else:
                    movie.is_watched = False
                    new_movie = Movie(movie[0], movie[1], movie[2], movie.is_watched)
                    self.movies.append(new_movie)

    def add_movie(self, new_movie):
        self.movies.append(new_movie)