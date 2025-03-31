from functools import reduce
from random import randint

from utils.game import Game


class SmallestCommonMultipleGame(Game):
    def __init__(self):
        super().__init__()

    def get_random_numbers(self):
        return [randint(1, 20) for _ in range(3)]

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return SmallestCommonMultipleGame.gcd(b, a % b)

    @staticmethod
    def scm(a, b):
        return abs(a * b) // SmallestCommonMultipleGame.gcd(a, b)

    @staticmethod
    def scm_tree(*args):
        return reduce(lambda x, y: SmallestCommonMultipleGame.scm(x, y), args)

    def play_round(self, round):
        print("Find the smallest common multiple of given numbers.")
        numbers = self.get_random_numbers()
        print(", ".join(map(str, numbers)))

        user_answer = input("Your answer: ").strip()
        if not user_answer:
            return False

        correct_answer = self.scm_tree(*numbers)
        self.compare_answer(user_answer, correct_answer)

        return True