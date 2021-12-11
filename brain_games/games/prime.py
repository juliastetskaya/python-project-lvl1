from brain_games.game import game
from brain_games.math import get_random_int, is_prime

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_data():
    number = get_random_int()

    correct_answer = 'yes' if is_prime(number) else 'no'

    return (number, correct_answer)


def prime():
    return game(rules, get_data)
