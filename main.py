"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""
# TODO: Create your main program in this file, using the MoviesToWatchApp class

from kivy.app import App
from movie import Movie
from moviecollection import MovieCollection
from kivy.lang import Builder
from kivy.core.window import Window


class MoviesToWatchApp(App):
    """..."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movies_to_watch = MovieCollection()
        self.movies_to_watch.load_movies('movies.csv')


if __name__ == '__main__':
    MoviesToWatchApp().run()
