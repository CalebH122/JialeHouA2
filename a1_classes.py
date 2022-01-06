"""..."""
# TODO: Copy your first assignment to this file, then update it to use Movie class
# Optionally, you may also use MovieCollection class

from movie import Movie
from moviecollection import MovieCollection

print("Movies to watch 1.0 - by Jiale Hou")

MENU = """Menu:
L - List movie
A - Add new movie
W - Watch a movie
Q - Quit"""


def main():
    """This is the main function(structure of this program), witch is include all functions under it."""
    movies = MovieCollection()
    movies.load_movies('movies.csv')
    print("{} movies are loaded".format(movies.watched_movie_num() + movies.un_watched_num()))
    movies.sort('year')  # Sort movie function. line 156
    user_input = input(f"{MENU}\n>>> ").upper()
    while user_input != 'Q':
        if user_input == 'L':
            show_movie(movies)  # Show movie function. line 43
            user_input = input(f"{MENU}\n>>> ").upper()
        elif user_input == 'A':
            add_movie(movies)  # Add movie function. line 57
            movies.sort('year')  # Sort movie function. line 156
            user_input = input(f"{MENU}\n>>> ").upper()
        elif user_input == 'W':
            watch_movie(movies)  # Watch movie function. line 113
            user_input = input(f"{MENU}\n>>> ").upper()
        else:
            print("Invalid menu choice")
            user_input = input(f"{MENU}\n>>> ").upper()
    movies.save_movies('movies.csv')  # Save movie information function. line 174
    print(f"{movies.watched_movie_num() + movies.un_watched_num()} movies saved to movies.csv\nHave a nice day :)")


def show_movie(movies):
    """This is the fist function, this function is designed to show all the movies in the list."""
    print(movies)


def add_movie(movies):
    """This function will collect information of new movie, and add it to the movie list"""
    movie_name = name_check()  # line 103
    movie_year = year_check()  # line 81
    movie_category = category_check()  # line 71
    movie_status = False
    print("{} ({} from {}) is added to movie list".format(movie_name, movie_category, movie_year))
    movies.add_movie(Movie(movie_name, movie_year, movie_category, movie_status))


def category_check():
    """This function will error check the category input, it will return the valid category input back to add
    movie function"""
    category = input("Category: ")
    while category == '':
        print("Input can not be blank")
        category = input("Category: ")
    return category


def year_check():
    """This function use try and expect to error check the year input, eventually it will return a valid number of year
     back to the add movie function"""
    year = input("Year: ")
    is_year_valid = False
    while not is_year_valid:
        try:
            year = int(year)
            if year <= 0:
                print("Number must be >= 0")
                year = input("Year: ")
            elif year == '':
                print("Invalid input; enter a valid number")
                year = input("Year: ")
            else:
                is_year_valid = True
                return year
        except ValueError:
            print("Invalid input; enter a valid number")
            year = input("Year: ")


def name_check():
    """This function also is part of add movie function, it will error check movie name and return it until it is
     valid."""
    name = input("Title: ")
    while name == '':
        print("Input can not be blank")
        name = input("Title: ")
    return name


def watch_movie(movies):
    """This is watch movie function. It will check if there is any movie not watched yet. If no, it will tell you there
    are no movie left for you to watch. If yes, you will have to enter the movie number to change the movie status as
    watched for the movie you want to watch. Also this function will error check your input for movie number."""
    if movies.un_watched_num() == 0:
        print("No more movies to watch!")
    else:
        movie_choice = input("Enter the number of a movie to mark as watched\n>>> ")
        is_valid = False
        while not is_valid:
            try:
                movie_choice = int(movie_choice)
                if movie_choice > movies.un_watched_num() + movies.watched_movie_num():
                    print("Invalid movie number")
                    movie_choice = input(">>> ")
                elif movie_choice < 0:
                    print("Number must >= 0")
                    movie_choice = input(">>> ")
                else:
                    is_valid = True
            except ValueError:
                print("Invalid input; enter a valid number")
                movie_choice = input(">>>")

        movie = movies.movies[movie_choice-1]
        if movie.is_watched is False:
            print(f"{movie.title} form {movie.year} watched")
            movie.watched()
        else:
            print(f"You have already watched {movie.title}")


def sort_movies(movies):
    """This function is designed to sort the movies in the list by year and alphabet order."""
    for movie in movies:
        movie[1] = int(movie[1])
    movies.sort(key=lambda x: (x[1], x[2]))


def save_movies(movies):
    """The final function, this function is to save all updated movie information back into the csv file."""
    save_file = open("movies.csv", 'w')
    for movie in movies:
        print(f"{movie[0]},{movie[1]},{movie[2]},{movie[3]}", file=save_file)
    save_file.close()


main()


