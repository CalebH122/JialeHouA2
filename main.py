"""
Name: Jiale Hou
Date: 1/12/2022
Brief Project Description: A Kivy GUI allows you load and save movies from csv file, add movie, sort movie and change
movie watch status.
GitHub URL: https://github.com/CalebH122/JialeHouA2
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
        """Initialise the app"""
        super().__init__(**kwargs)
        self.movies_to_watch = MovieCollection()
        self.movies_to_watch.load_movies('movies.csv')

    def build(self):
        """build app from kivy file"""
        self.title = "Movie to watch 2.0"
        self.root = Builder.load_file('app.kv')
        self.load_movies()
        self.sort(self.root.ids.sort.text)
        return self.root

    def load_movies(self):
        """show all the movie in list"""
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
            self.root.ids.watch_movie_status.text = f'To watch: {self.movies_to_watch.un_watched_num()}. Watched: {self.movies_to_watch.watched_movie_num()} '

    def sort(self, sort_choice):
        """Sort all movies by sort choice"""
        self.movies_to_watch.sort(sort_choice)
        self.root.ids.movie_list.clear_widgets()
        self.load_movies()

    def change_button(self, button):
        """Change the movie status and change the button when pressing"""
        for i, movie in enumerate(self.movies_to_watch.movies):
            if i == button.id:
                if movie.is_watched:
                    movie.is_watched = False
                    self.root.ids.movie_list.clear_widgets()
                    self.load_movies()
                    if movie.is_watched:
                        self.root.ids.announcement.text = f'You have watched {movie.title}'
                    else:
                        self.root.ids.announcement.text = f'You need to watch {movie.title}'
                else:
                    movie.is_watched = True
                    self.root.ids.movie_list.clear_widgets()
                    self.load_movies()
                    if movie.is_watched:
                        self.root.ids.announcement.text = f'You have watched {movie.title}'
                    else:
                        self.root.ids.announcement.text = f'You need to watch {movie.title}'
        self.sort(self.root.ids.sort.text)

    def add_movie(self):
        """Add movie in to movie list"""
        category_list = ['Action', 'Comedy', 'Documentary', 'Drama', 'Fantasy', 'Thriller']
        try:
            if self.root.ids.title.text == '':
                self.root.ids.announcement.text = 'All fields are must be completed'
            elif self.root.ids.year.text == '':
                self.root.ids.announcement.text = 'All fields are must be completed'
            elif self.root.ids.category.text == '':
                self.root.ids.announcement.text = 'All fields are must be completed'
            elif int(self.root.ids.year.text) <= 0:
                self.root.ids.announcement.text = 'Year must be > 0'
            elif self.root.ids.category.text not in category_list:
                self.root.ids.announcement.text = 'Category must be one of Action, Comedy, Documentary, Drama, ' \
                                                  'Fantasy, Thriller '
            else:
                self.movies_to_watch.add_movie(
                    Movie(self.root.ids.title.text, int(self.root.ids.year.text), self.root.ids.category.text,
                          False))
                self.load_movies()
                self.root.ids.announcement.text = ''
                self.root.ids.title.text = ''
                self.root.ids.year.text = ''
                self.root.ids.category.text = ''
                self.sort(self.root.ids.sort.text)
        except ValueError:
            self.root.ids.announcement.text = 'Please enter a valid number'

    def clear_text(self):
        """Clear all text in text filed"""
        self.root.ids.title.text = ""
        self.root.ids.year.text = ""
        self.root.ids.category.text = ""
        self.root.ids.announcement.text = ""

    def on_stop(self):
        """Save all movie in to csv file when you close the app"""
        self.movies_to_watch.save_movies('movies.csv')


if __name__ == '__main__':
    MoviesToWatchApp().run()
