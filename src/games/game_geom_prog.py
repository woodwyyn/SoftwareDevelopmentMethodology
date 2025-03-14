from random import randint

from utils.hello import welcome_message
from utils.messages import (
    CORRECT_ANSWER_MESSAGE,
    END_GAME_INSTRUCTION,
    GAME_OVER_MESSAGE,
    INCORRECT_ANSWER_MESSAGE,
    LEVEL_GAME,
    QUESTION_TEMPLATE,
)


def get_geometric_progression(difficulty):
    if difficulty == "easy":
        first_term, ratio = randint(1, 5), randint(2, 3)
    elif difficulty == "normal":
        first_term, ratio = randint(1, 5), randint(2, 6)
    elif difficulty == "hard":
        first_term, ratio = randint(1, 20), randint(2, 7)

    return [first_term * ratio**i for i in range(10)]


def hide_element(progression):
    index_hidden = randint(0, len(progression) - 1)
    element_hidden = progression[index_hidden]
    progression[index_hidden] = ".."
    return progression, element_hidden


def game(progression):
    question = QUESTION_TEMPLATE.format(", ".join(map(str, progression)))
    print(question)
    
    answer = input("Your answer: ").strip()
    return answer


def check_answer(correct_answer, user_answer, player_name):
    if int(user_answer) == correct_answer:
        print(CORRECT_ANSWER_MESSAGE)
    else:
        print(INCORRECT_ANSWER_MESSAGE.format(user_answer, correct_answer, player_name))


def play_game(name, difficulty):
    print("\nWhat number is missing in this geometric progression?")
    print(END_GAME_INSTRUCTION)

    while True:
        progression, correct_answer = hide_element(get_geometric_progression(difficulty))
        
        user_answer = game(progression)
        
        if not user_answer:
            print(GAME_OVER_MESSAGE.format(name))
            break
            
        check_answer(correct_answer, user_answer, name)


if __name__ == "__main__":
    player_name = welcome_message()
    difficulty = input(LEVEL_GAME).lower().strip()

    if not difficulty or difficulty not in ["normal", "hard"]:
        difficulty = "easy"
    play_game(player_name, difficulty)
