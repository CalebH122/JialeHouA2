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
from kivy.uix.button import Button


class MoviesToWatchApp(App):
    """..."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = "Movie to watch 2.0"
        self.movies_to_watch = MovieCollection()
        self.movies_to_watch.load_movies('movies.csv')

    def build(self):
        self.title = "Movie to watch 2.0"
        self.root = Builder.load_file('app.kv')
        self.load_movies()
        return self.root

    def load_movies(self):
        for i, movie in enumerate(self.movies_to_watch.movies):
            movie_button = Button()
            movie_button.id = i
            if movie.is_watched:
                movie.is_watched = 'Watched'
                movie_button.background_color = (0.8, 1, 0, 1)
            else:
                movie.is_watched = ''
                movie_button.background_color = (0.1, 0.8, 0.8, 1)
            movie_button.text = f'{movie.title} ({movie.category} from {movie.year}) {movie.is_watched}'
            self.root.ids.movie_list.add_widget(movie_button)


if __name__ == '__main__':
    MoviesToWatchApp().run()
