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
        self.movies_to_watch = MovieCollection()
        self.movies_to_watch.load_movies('movies.csv')

    def build(self):
        self.title = "Movie to watch 2.0"
        self.root = Builder.load_file('app.kv')
        self.load_movies()
        self.sort('category')
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
            movie_button.bind(on_press=self.change_button)
            self.root.ids.watch_movie_status.text = f'To watch: {self.movies_to_watch.un_watched_num()}. Watched: {self.movies_to_watch.watched_movie_num()}'

    def sort(self, sort_choice):
        self.movies_to_watch.sort(sort_choice)
        self.root.ids.movie_list.clear_widgets()
        self.load_movies()

    def change_button(self, button):
        for i, movie in enumerate(self.movies_to_watch.movies):
            if i == button.id:
                if movie.is_watched:
                    movie.is_watched = False
                    self.root.ids.movie_list.clear_widgets()
                    self.load_movies()
                else:
                    movie.is_watched = True
                    self.root.ids.movie_list.clear_widgets()
                    self.load_movies()
        self.sort(self.root.ids.sort.text)


if __name__ == '__main__':
    MoviesToWatchApp().run()
