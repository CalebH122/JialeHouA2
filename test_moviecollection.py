"""(Incomplete) Tests for MovieCollection class."""
from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies  # an empty list is considered False

    # Test loading movies
    print("Test loading movies:")
    movie_collection.load_movies('movies.csv')
    print(movie_collection)
    assert movie_collection.movies  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Movie with values
    print("Test adding new movie:")
    movie_collection.add_movie(Movie("Amazing Grace", 2006, "Drama", False))
    print(movie_collection)

    # Test sorting movies
    print("Test sorting - year:")
    movie_collection.sort("year")
    print(movie_collection)
    # TODO: Add more sorting tests
    print("New sorting test - title:")
    movie_collection.sort("title")
    print(movie_collection)

    print("New sorting test - category:")
    movie_collection.sort("category")
    print(movie_collection)
    # TODO: Test saving movies (check CSV file manually to see results)
    movie_collection.save_movies('movies.csv')
    # TODO: Add more tests, as appropriate, for each method
    print("Final test: ")
    movie_collection.watched()
    movie_collection.movies.clear()
    movie_collection.load_movies('movies.csv')
    movie_collection.add_movie(Movie("ABCDEFG", 1234, "Action", True))
    movie_collection.sort("year")
    print(f"Watched movie number: {movie_collection.watched_movie_num()}")
    print(f"Un-watch movie number: {movie_collection.un_watched_num()}")
    print(movie_collection)


run_tests()
