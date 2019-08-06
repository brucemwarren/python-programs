# Program to print out the lyrics to "99 Bottles of Beer (On The Wall)"
#
# The Rules:
#
# If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in
# function.
# Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
# Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
# Put a blank line between each verse of the song.
# Project from: https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/

def bottles_of_beer(count):
    """
    Very simple function that will take a number of bottles of beer and sing the song.
    :param count:
    :return:
    """
    if int(count) == count:

        bottles = count

        while bottles > 1:  # While the count is greater than 1, it will print the lyric, plus a blank line.
            print(bottles, "bottles of beer on the wall!", bottles, "bottles of beeeeer! Take one down and pass it around",
                  (bottles - 1), "bottles of beer on the wall!!!!")
            print()
            bottles = bottles - 1  # Adjusts the bottle count
        else:
            # Adjusts the lyrics for the last bottle.
            print(bottles, "bottle of beer on the wall!", bottles,
                  "bottle of beeeeer! Take it down and pass it around, no more bottles of beer on the wall!!!!")
    else:
        print("Please enter a number")


bottles_of_beer(6.0)
