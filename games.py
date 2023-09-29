import os
import time
from math import ceil
from statistics import mean
from random import randint

time_limit = 1  # todo: create mode without timer


def multiplication(mode):
    # todo: add beginning print + and tip on how to solve + maybe start button
    os.system("clear")
    response_time = []
    wrong_answers = []

    # todo: lmfao refactor tf out of this
    type_dict = {
        "base10": [[19, 19], [10, 19]],
        "twoBy1": [[10, 99], [2, 9]],
        "twoBy2": [[10, 99], [10, 99]]
    }
    random_range1 = type_dict[mode][0]
    random_range2 = type_dict[mode][1]

    t_end = time.time() + 60 * time_limit
    while time.time() < t_end:

        question_start_time = time.time()

        num_1, num_2 = randint(random_range1[0], random_range1[1]), randint(random_range2[0], random_range2[1])
        answer = num_1 * num_2
        question = f"{num_1} x {num_2}"

        # todo: abstract getting user input into a method
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
        print(f"Your average time to mentally compute is {ceil(mean(response_time))} seconds.\n")  # todo: rephrase

    # Provide questions answered wrong
    if wrong_answers:
        print("\nYou got the following questions wrong:")
        for answer in wrong_answers:
            print(f"{answer[0]}; {answer[1]}")  # todo: return as a table


def fraction_conversion():
    pass


def decimal_conversion():
    pass


def percentages():
    pass
