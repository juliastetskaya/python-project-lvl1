from brain_games.game import game
from brain_games.math import get_random_int, is_even

rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_data():
    number = get_random_int()
    correct_answer = 'yes' if is_even(number) else 'no'

    return (number, correct_answer)


def even():
    return game(rules, get_data)
