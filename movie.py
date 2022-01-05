"""..."""


# TODO: Create your Movie class in this file


class Movie:
    """..."""

    def __init__(self, title="", year=0, category="", is_watched=False):
        self.is_watched = True
        self.title = title
        self.category = category
        self.year = year
        if is_watched == "u":
            is_watched = False
        elif is_watched == "w":
            is_watched = True
        else:
            pass
        self.is_watched = is_watched

    def not_watch(self):
        self.is_watched = False

    def watched(self):
        self.is_watched = True

    def __str__(self):
        return f"{self.title:35} {self.category:6} {self.year:<4} {self.is_watched}"

