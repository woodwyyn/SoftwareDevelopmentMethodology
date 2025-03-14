from functools import reduce
from random import randint

from utils.hello import welcome_message
from utils.game import game
from utils.messages import (
    CORRECT_ANSWER_MESSAGE,
    END_GAME_INSTRUCTION,
    GAME_OVER_MESSAGE,
    INCORRECT_ANSWER_MESSAGE,
    QUESTION_TEMPLATE,
)


def get_random_numbers(min_val=1, max_val=20):
    return [randint(min_val, max_val) for _ in range(3)]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def scm(a, b):
    return abs(a * b) // gcd(a, b)


def scm_tree(*args):
    return reduce(lambda x, y: scm(x, y), args)

def check_answer(correct_answer, user_answer, player_name):
    if user_answer == correct_answer:
        print(CORRECT_ANSWER_MESSAGE)
    else:
        print(INCORRECT_ANSWER_MESSAGE.format(user_answer, correct_answer, player_name))

def play_game(name):
    print("\nFind the smallest common multiple of given numbers.")
    print(END_GAME_INSTRUCTION)

    while True:
        numbers = get_random_numbers()

        user_answer = game(numbers)

        if not user_answer:
            print(GAME_OVER_MESSAGE.format(name))
            break

        check_answer(scm_tree(*numbers), int(user_answer), name)


if __name__ == "__main__":
    player_name = welcome_message()
    play_game(player_name)
