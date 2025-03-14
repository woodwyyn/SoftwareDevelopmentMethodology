from .messages import QUESTION_TEMPLATE

def game(numbers):
	question = QUESTION_TEMPLATE.format(", ".join(map(str, numbers)))
	print(question)
	answer = input("Your answer: ").strip()
    
	return answer