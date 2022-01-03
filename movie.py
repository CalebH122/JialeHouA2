"""..."""


# TODO: Create your Movie class in this file


class Movie:
    """..."""

    def __init__(self, title="", category="", year=0, is_watched=""):
        self.is_watched = True
        self.title = title
        self.category = category
        self.year = year
        self.is_watch = is_watched

    def is_watched(self):
        if not self.is_watch:
            self.is_watched = 'u'
            return self.is_watched
        else:
            self.is_watched = 'w'
            return self.is_watched

    def __str__(self):
        return f"Title: {self.title} Category: {self.category} Year: {self.year} Watched: {self.is_watched}"
