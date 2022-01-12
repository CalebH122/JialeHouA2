"""Name: Jiale Hou
Date: 1/12/2022
Brief Project Description: MovieCollection class
GitHub URL: https://github.com/CalebH122/JialeHouA2
"""

# TODO: Create your MovieCollection class in this file
from movie import Movie
import csv
from operator import attrgetter


class MovieCollection(Movie):
    """This is MovieCollection class"""

    def __init__(self):
        """initialization of MoiveCollection class"""
        super().__init__()
        self.movies = []

    def __str__(self):
        """Print the movie information in MovieCollection as a string"""
        if not self.movies:
            return "No movie"
        else:
            return '\n'.join(f"{num + 1}. {movie}" for num, movie in enumerate(self.movies))

    def load_movies(self, file):
        """Load the movies information in the file"""
        with open(file, 'r') as movie_file:
            movies = csv.reader(movie_file)
            for movie in movies:
                new_movie = Movie(movie[0], int(movie[1]), movie[2], movie[3])
                self.movies.append(new_movie)
        movie_file.close()

    def add_movie(self, new_movie):
        """Add movie in list"""
        self.movies.append(new_movie)

    def sort(self, sort_choice):
        """Sort all movie by sort choice then by year"""
        self.movies = sorted(self.movies, key=attrgetter(sort_choice, 'year'))

    def save_movies(self, file):
        """Save all the movies into csv file"""
        save_file = open(file, 'w')
        for movie in self.movies:
            if movie.is_watched is True or movie.is_watched == 'Watched':
                movie.is_watched = 'w'
            else:
                movie.is_watched = 'u'
            input_movie = f"{movie.title},{movie.year},{movie.category},{movie.is_watched}"
            print(input_movie, file=save_file)
        save_file.close()

    def un_watched_num(self):
        """count the number of movie un-watched"""
        un_watched_movies = 0
        for movie in self.movies:
            if not movie.is_watched:
                un_watched_movies += 1
        return un_watched_movies

    def watched_movie_num(self):
        """count the number of movie watched"""
        watched_movies = 0
        for movie in self.movies:
            if movie.is_watched:
                watched_movies += 1
        return watched_movies
