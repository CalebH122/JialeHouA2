"""(Incomplete) Tests for Movie class."""
from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert not default_movie.is_watched

    # Test initial-value movie
    print("Initial movie:")
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    print(initial_movie)
    # TODO: Write tests to show this initialisation works
    print("Movie two:")
    movie_two = Movie("Star war", 1997, "Action", False)
    print(movie_two)
    # TODO: Add more tests, as appropriate, for each method
    print("Movie three:")
    movie_three = Movie("The fugitive", 1993, "Drama", True)
    print(movie_three)

    print("Movie four:")
    movie_four = Movie()
    movie_four.title = "LALALA"
    movie_four.year = 2022
    movie_four.category = "Action"
    movie_four.is_watched = True
    print(movie_four)

run_tests()
