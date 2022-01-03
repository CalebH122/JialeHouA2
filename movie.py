"""..."""


# TODO: Create your Movie class in this file


class Movie:
    """..."""

    def __init__(self, title="", category="", year=0, is_watch=""):
        self.title = title
        self.category = category
        self.year = year
        self.is_watch = is_watch

    def is_watch(self):
        if not self.is_watch:
            self.is_watch = False
            return self.is_watch
        else:
            self.is_watch = True
            return self.is_watch
