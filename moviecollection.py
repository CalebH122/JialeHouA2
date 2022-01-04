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
                if movie.is_watched:
                    status = "Watched"
                    Movie(movie.title, movie.year, movie.category, status)
                else:
                    status = "Un-watch"
                    Movie(movie.title, movie.year, movie.category, status)

    def load_movies(self, file):
        with open(file, 'r') as movie_file:
            movies = csv.reader(movie_file)
            for movie in movies:
                new_movie = Movie(movie[0], movie[1], movie[2], movie[3])
                self.movies.append(new_movie)
        movie_file.close()

    def add_movie(self, new_movie):
        self.movies.append(new_movie)
