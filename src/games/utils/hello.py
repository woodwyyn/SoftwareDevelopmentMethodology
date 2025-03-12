from .messages import HELLO_MESSAGE, QUESTION_NAME, WELCOME_MESSAGE


def welcome_message():
    print(WELCOME_MESSAGE)
    name = input(QUESTION_NAME)
    print(HELLO_MESSAGE.format(name))
    return name
