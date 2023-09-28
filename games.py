import time
from math import ceil
from statistics import mean
from random import randint


time_limit = 0.5  # todo: create mode without timer
# todo: simplify construction of multiplication games - just changing the num int rang


def base10_multiplication():

    # todo: add beginning print + and tip on how to solve + maybe start button
    response_time = []
    wrong_answers = []

    t_end = time.time() + 60 * time_limit
    while time.time() < t_end:

        question_start_time = time.time()

        num_1, num_2 = randint(10, 20), randint(10, 20)
        answer = num_1 * num_2
        question = f"{num_1} x {num_2}"
        user_answer = input(f"{question} = ")

        # Error handling: Non-int user input
        if not user_answer.isnumeric():
            user_answer = input("> ")

        # Check answer
        if int(user_answer) == answer:
            question_end_time = time.time()
            response_time.append(ceil(question_end_time - question_start_time))

        else:
            print("Incorrect, you only get one shot at life!")
            wrong_answers.append([f"{question} = {answer}", user_answer])

    # todo: store scores
    print(f"\nYou got {len(response_time)} out of {len(response_time) + len(wrong_answers)} questions correct!")

    # Provide average computation time
    if response_time:
        print(f"Your average time to mentally compute is {ceil(mean(response_time))}\n")  # todo: rephrase

    # Provide questions answered wrong
    if wrong_answers:
        print("\nYou got the following questions wrong:")
        for answer in wrong_answers:
            print(f"{answer[0]}; {answer[1]}")  # todo: return as a table


def twoBy1_multiplication():
    pass # todo: Add message that game is in construction and select another game

def twoBy2_multiplication():
    pass

def fraction_conversion():
    pass

def decimal_conversion():
    pass

def percentages():
    pass
