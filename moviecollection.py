"""..."""

# TODO: Create your MovieCollection class in this file
from movie import Movie
import csv
from operator import attrgetter


class MovieCollection(Movie):
    """..."""

    def __init__(self):
        super().__init__()
        self.movies = []

    def __str__(self):
        if not self.movies:
            return "No movie"
        else:
            return '\n'.join(f"{num+1}. {movie}" for num, movie in enumerate(self.movies))

    def load_movies(self, file):
        with open(file, 'r') as movie_file:
            movies = csv.reader(movie_file)
            for movie in movies:
                new_movie = Movie(movie[0], int(movie[1]), movie[2], movie[3])
                self.movies.append(new_movie)
        movie_file.close()

    def add_movie(self, new_movie):
        self.movies.append(new_movie)

    def sort(self, sort_choice):
        self.movies = sorted(self.movies, key=attrgetter(sort_choice))

    def save_movies(self, file):
        save_file = open(file, 'w')
        for movie in self.movies:
            if movie.is_watched is True:
                movie.is_watched = 'w'
            else:
                movie.is_watched = 'u'
            input_movie = f"{movie.title},{movie.year},{movie.category},{movie.is_watched}"
            print(input_movie, file=save_file)
        save_file.close()

    def un_watched_num(self):
        un_watched_movies = 0
        for movie in self.movies:
            if not movie.is_watched:
                un_watched_movies += 1
        return un_watched_movies

    def watched_movie_num(self):
        watched_movies = 0
        for movie in self.movies:
            if movie.is_watched:
                watched_movies += 1
        return watched_movies
