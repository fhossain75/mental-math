import os
import time
import json
from math import ceil
from statistics import mean
from random import randint

time_limit = 1
score_board_file = 'scoreBoard.json'


def get_score_board_data():
    with open(score_board_file, 'r') as f:
        score_board = json.load(f)

    return score_board


def set_score_board_data(updated_score_board):

    with open(score_board_file, 'w') as fp:
        json.dump(updated_score_board, fp)


def multiplication(mode):
    # todo: add beginning print
    os.system("clear")
    response_time = []
    wrong_answers = []

    # todo: lmfao refactor tf out of this
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

    # Output results
    correct_answer_count = len(response_time)
    incorrect_answer_count = len(wrong_answers)
    avg_response_time = ceil(mean(response_time))

    print(f"\nYou got {correct_answer_count} out of {correct_answer_count + incorrect_answer_count} questions correct!")

    # Provide average computation time
    if response_time:
        print(f"Your average time to mentally compute is {avg_response_time} seconds.\n")  # todo: rephrase

    # Provide questions answered wrong
    if wrong_answers:
        print("\nYou got the following questions wrong:")
        for answer in wrong_answers:
            print(f"{answer[0]}; {answer[1]}")  # todo: return as a table

    # Update score_board
    score_board = get_score_board_data()
    high_score, best_time = score_board["maxCorrect"], score_board["bestTime"]

    if correct_answer_count > high_score:
        score_board["maxCorrect"] = correct_answer_count
        print(f"\nYou beat your high score of {high_score}")
    else:
        print(f"\nCurrent high score is {high_score}")

    if best_time > avg_response_time:
        score_board["bestTime"] = correct_answer_count
        print(f"\nThis has been your fastest time yet! You beat your previous best time of {best_time} secs.")
    else:
        print(f"\nCurrent best time is {best_time} secs.")


def fraction_conversion():
    pass


def decimal_conversion():
    pass


def percentages():
    pass
