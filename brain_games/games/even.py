from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
START_NUMBER = 0
END_NUMBER = 100


def is_even(num):
    return num % 2 == 0


def get_game_data():
    number = randint(START_NUMBER, END_NUMBER)
    correct_answer = 'yes' if is_even(number) else 'no'

    return (number, correct_answer)
