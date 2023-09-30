import json
from math import ceil
from statistics import mean


score_board_file = 'scoreBoard.json'


def get_user_answer(question):
    user_answer = input(f"{question} = ")

    # Error handling: Non-int user input
    while not user_answer.isnumeric():
        user_answer = input("> ")

    return user_answer


def output_game_results(response_time, wrong_answers):

    # Calculate results
    correct_answer_count = len(response_time)
    incorrect_answer_count = len(wrong_answers)
    avg_response_time = ceil(mean(response_time))

    # Provide number of correct answers
    print(f"\nYou got {correct_answer_count} out of {correct_answer_count + incorrect_answer_count} questions correct.")

    # Provide average computation time
    if response_time:
        print(f"Average time of {avg_response_time} seconds.")  # todo: rephrase

    # Output & update score board
    output_score_board_results(avg_response_time, correct_answer_count)

    # Provide number of incorrect answers
    if wrong_answers:
        print("\nYou got the following questions wrong:")
        for answer in wrong_answers:
            print(f"{answer[0]}; {answer[1]}")  # todo: return as a table
        print()


def get_score_board_data():
    with open(score_board_file, 'r') as f:
        score_board = json.load(f)

    return score_board


def set_score_board_data(updated_score_board):
    with open(score_board_file, 'w') as fp:
        json.dump(updated_score_board, fp)


def output_score_board_results(avg_response_time, correct_answer_count):

    # Init variables
    score_board = get_score_board_data()
    high_score, best_time = score_board["maxCorrect"], score_board["bestTime"]
    score_board_changed = False

    # Update & output high score
    if correct_answer_count > high_score:
        score_board["maxCorrect"] = correct_answer_count
        score_board_changed = True
        print(f"\nYou beat your high score of {high_score}!")
    else:
        print(f"Current high score is {high_score}")

    # Update & output best time
    if best_time < avg_response_time:
        score_board["bestTime"] = best_time
        score_board_changed = True
        print(f"This has been your fastest time yet! You beat your previous best time of {best_time} secs.")
    else:
        print(f"Current best time is {best_time} secs.")

    # Update score board
    if score_board_changed:
        set_score_board_data(score_board)
