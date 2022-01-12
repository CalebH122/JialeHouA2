"""Name: Jiale Hou
Date: 1/12/2022
Brief Project Description: Movie class
GitHub URL: https://github.com/CalebH122/JialeHouA2
"""


# TODO: Create your Movie class in this file


class Movie:
    """This will represent as a movie object"""

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
        """Change movie status to un_watch"""
        self.is_watched = False

    def watched(self):
        """Change movie status to watched"""
        self.is_watched = True

    def __str__(self):
        """print string to show movie information"""
        return f"{self.title} {self.year} {self.category} {self.is_watched}"

