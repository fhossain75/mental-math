def start_game():
    # todo: Add ASCII Art & change color
    # todo: reword "select..."
    print("\n Welcome to Math Practice\
          \n Here you will be timed to complete the most amount of math problems.\
          \n Select the math you want to improve on:\
          \n A - Base 10 Multiplication\
          \n B - 2 x 1 Digit Multiplication\
          \n C - 2 x 2 Digit Multiplication\
          \n D - Fraction Conversion\
          \n E - Decimal Conversion\
          \n F - Percentage\
          \n @ - All The Above")

    # Get user input
    user_choice = ""
    selection_options = [chr[ASCII] for ASCII in range(97,123)]
    while user_choice not in selection_options:
        user_choice = input("> ")

    # Handle user choice
    if user_choice == "A":
        pass
    else:
        print("That's not one of the choices! Try again.\n")



