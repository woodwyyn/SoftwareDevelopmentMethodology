from random import randint

from utils.game import Game
from utils.messages import (
    CHOOSE_LEVEL,
    END_GAME_INSTRUCTION,
    LEVEL_GAME,
)


class GeometricProgressionGame(Game):
    def __init__(self):
        super().__init__()
        self.difficulty = None

    def set_difficulty(self, difficulty):
        if difficulty in ["easy", "normal", "hard"]:
            self.difficulty = difficulty
        else:
            self.difficulty = "easy"
        
        print(CHOOSE_LEVEL.format(self.difficulty))

    def get_geometric_progression(self):
        if self.difficulty == "easy":
            first_term, ratio = randint(1, 5), randint(2, 3)
        elif self.difficulty == "normal":
            first_term, ratio = randint(1, 5), randint(2, 6)
        elif self.difficulty == "hard":
            first_term, ratio = randint(1, 20), randint(2, 7)
        else:
            first_term, ratio = 1, 2

        return [first_term * ratio**i for i in range(10)]

    def hide_element(self, progression):
        index_hidden = randint(0, len(progression) - 1)
        element_hidden = progression[index_hidden]
        progression[index_hidden] = ".."
        return progression, element_hidden

    def play_round(self, round):
        print("What number is missing in this geometric progression?")
        print(END_GAME_INSTRUCTION)

        progression, correct_answer = self.hide_element(self.get_geometric_progression())
        print(" ".join(map(str, progression)))

        user_answer = input("Your answer: ").strip()
        if not user_answer:
            return False

        self.compare_answer(int(user_answer), correct_answer)

        return True
    
    def choose_difficulty(self):
        difficulty = input(LEVEL_GAME).lower().strip()
        self.set_difficulty(difficulty)