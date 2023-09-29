import os
import time
from random import randint
from utils import *


time_limit = 1


def multiplication(mode):
    # todo: add beginning print
    os.system("clear")
    response_time = []
    wrong_answers = []

    type_dict = {
        "base10": [[10, 19], [10, 19]],
        "twoBy1": [[10, 99], [2, 9]],
        "twoBy2": [[10, 99], [10, 99]]
    }
    random_range1 = type_dict[mode][0]
    random_range2 = type_dict[mode][1]

    t_end = time.time() + 60 * time_limit
    while time.time() < t_end:

        question_start_time = time.time()

        num_1 = randint(random_range1[0], random_range1[1])
        num_2 = randint(random_range2[0], random_range2[1])
        question = f"{num_1} x {num_2}"
        answer = num_1 * num_2

        user_answer = get_user_answer(question)

        # Check answer
        if int(user_answer) == answer:
            question_end_time = time.time()
            response_time.append(ceil(question_end_time - question_start_time))

        else:
            print("Incorrect, you only get one shot at life!")
            wrong_answers.append([f"{question} = {answer}", user_answer])

    # Output results
    output_game_results(response_time, wrong_answers)


def fraction_conversion():
    pass


def decimal_conversion():
    pass


def percentages():
    pass
