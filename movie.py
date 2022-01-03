"""..."""


# TODO: Create your Movie class in this file


class Movie:
    """..."""

    def __init__(self, title="", category="", year=0, is_watched=False):
        self.is_watched = True
        self.title = title
        self.category = category
        self.year = year
        self.is_watched = is_watched

    def not_watch(self):
        if self.is_watched is False:
            self.is_watched = 'Unwatch'

    def watched(self):
        if self.is_watched is True:
            self.is_watched = 'Watched'

    def __str__(self):
        return f"Title: {self.title} Category: {self.category} Year: {self.year} Watched: {self.is_watched}"
