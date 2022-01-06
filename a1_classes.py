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
    movies = MovieCollection()  # Load function. line 163
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
            sort_movies(movies)  # Sort movie function. line 156
            user_input = input(f"{MENU}\n>>> ").upper()
        elif user_input == 'W':
            watch_movie(movies)  # Watch movie function. line 113
            user_input = input(f"{MENU}\n>>> ").upper()
        else:
            print("Invalid menu choice")
            user_input = input(f"{MENU}\n>>> ").upper()
    save_movies(movies)  # Save movie information function. line 174
    print("{} movies saved to movies.csv\nHave a nice day :)".format(len(movies)))


def show_movie(movies):
    """This is the fist function, this function is designed to show all the movies in the list."""
    watched_movie = 0
    unwatch_movie = 0
    for num, movie in enumerate(movies):
        if movie[3] == 'u':
            unwatch_movie = unwatch_movie + 1
            print(f"{num}. *  {movie[0]:<35} - {movie[1]:>4} ({movie[2]})")
        else:
            watched_movie = watched_movie + 1
            print(f"{num}.    {movie[0]:<35} - {movie[1]:>4} ({movie[2]})")
    print("{} movies watched, {} movies still to watch.".format(watched_movie, unwatch_movie))


def add_movie(movies):
    """This function will collect information of new movie, and add it to the movie list"""
    new_movie = []
    movie_name = name_check()  # line 103
    new_movie.append(movie_name)
    movie_year = year_check()  # line 81
    new_movie.append(movie_year)
    movie_category = category_check()  # line 71
    new_movie.append(movie_category)
    movie_status = 'u'
    new_movie.append(movie_status)
    print("{} ({} from {}) is added to movie list".format(movie_name, movie_category, movie_year))
    movies.append(new_movie)


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
    unwatch_movie = movie_count(movies)  # Count unwatch movie function. line 143
    if unwatch_movie == 0:
        print("No more movies to watch!")
    else:
        movie_choice = input("Enter the number of a movie to mark as watched\n>>> ")
        is_valid = False
        while not is_valid:
            try:
                movie_choice = int(movie_choice)
                if movie_choice > len(movies) - 1:
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

        movie = movies[movie_choice]
        if movie[3] == 'u':
            print(f"{movie[0]} form {movie[1]} watched")
            movie[3] = 'w'
        else:
            print(f"You have already watched {movie[0]}")


def movie_count(movies):
    """This function will count how many unwatch movies are there, this function is important
     for watch movie function."""
    unwatch_movie = 0
    for movie in movies:
        if movie[3] == 'u':
            unwatch_movie = unwatch_movie + 1
    return unwatch_movie


def sort_movies(movies):
    """This function is designed to sort the movies in the list by year and alphabet order."""
    for movie in movies:
        movie[1] = int(movie[1])
    movies.sort(key=lambda x: (x[1], x[2]))


def load_movies():
    """This function is the very first function, it will load movie information into a list for further modification."""
    movies = open("movies.csv", 'r')
    movie_list = []
    for line in movies:
        movie = line.strip().split(',')
        movie_list.append(movie)
    movies.close()
    return movie_list


def save_movies(movies):
    """The final function, this function is to save all updated movie information back into the csv file."""
    save_file = open("movies.csv", 'w')
    for movie in movies:
        print(f"{movie[0]},{movie[1]},{movie[2]},{movie[3]}", file=save_file)
    save_file.close()


main()


