from games import *


def start_game():
    # todo: Add ASCII Art & change color
    print("\n Welcome to Math Practice!\
          \n Here you will be timed to complete the most amount of math problems.\
          \n Select the math you want to improve on:\n\
          \n A - Base 10 Multiplication\
          \n B - 2 x 1 Digit Multiplication\
          \n C - 2 x 2 Digit Multiplication\
          \n D - Fraction Conversion\
          \n E - Decimal Conversion\
          \n F - Percentages\
          \n @ - All The Above\n")

    # print("Do you want to learn mental math tricks or practice problems?\
    #       \n 1 - Learn\
    #       \n 2 - Practice")

    # todo: Two modes: one with timer and one without and provides average time to calculate

    # Get user input
    user_choice = input("> ")
    selection_options = [chr(ascii_code) for ascii_code in range(65, 65 + 7)]

    while user_choice not in selection_options:
        print("That's not one of the choices! Try again.\n")
        user_choice = input("> ")

    game_type_dict = {
        'A': base10_multiplication,
        'B': twoBy1_multiplication,
        'C': twoBy2_multiplication,
        'D': fraction_conversion,
        'E': decimal_conversion,
        'F': percentages
    }

    # Handle user choice
    game_type_dict[user_choice]()


if __name__ == "__main__":
    start_game()
