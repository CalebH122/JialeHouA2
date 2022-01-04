"""..."""


# TODO: Create your MovieCollection class in this file
from movie import Movie


class MovieCollection(Movie):
    """..."""

    def __init__(self):
        super().__init__()
        self.movies = []

    def __str__(self):
        if not self.movies:
            print("No movie")




