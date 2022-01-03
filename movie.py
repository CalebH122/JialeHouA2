"""..."""


# TODO: Create your Movie class in this file


class Movie:
    """..."""

    def __init__(self, title="", year=0, category="", is_watched=False):
        self.is_watched = True
        self.title = title
        self.category = category
        self.year = year
        self.is_watched = is_watched

    def not_watch(self):
        if not self.is_watched:
            self.is_watched = "Unwatch"
            return self.is_watched

    def watched(self):
        if self.is_watched:
            self.is_watched = "Watched"
            return self.is_watched

    def __str__(self):
        return f"Title: {self.title} Category: {self.category} Year: {self.year} Watched: {self.is_watched}"
