from .messages import (
	CORRECT_ANSWER_MESSAGE,
	GAME_OVER_MESSAGE,
	HELLO_MESSAGE,
	INCORRECT_ANSWER_MESSAGE,
	QUESTION_NAME,
	ROUND_NUMBER,
	WELCOME_MESSAGE,
)


class Game:
	def __init__(self):
		self.rounds = 3
		self.name = None

	def start(self):
		self.name = self.welcome_message()

		for round in range(1, self.rounds + 1):
			print(ROUND_NUMBER.format(round))
			if not self.play_round(round):
				print()
				break

		print(GAME_OVER_MESSAGE.format(self.name))
			
	def compare_answer(self, user_answer, correct_answer):
		try:
			user_answer_int = int(user_answer)
			
			if user_answer_int == correct_answer:
				print(CORRECT_ANSWER_MESSAGE)
			else:
				print(INCORRECT_ANSWER_MESSAGE.format(user_answer, correct_answer, self.name))
		
		except ValueError:
			print("Invalid input number.")

	def play_round(self, round):
		pass

	def welcome_message(self):
		print(WELCOME_MESSAGE)
		name = input(QUESTION_NAME)
		print(HELLO_MESSAGE.format(name))
		return name

