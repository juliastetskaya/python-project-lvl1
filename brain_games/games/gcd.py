from brain_games.game import game
from brain_games.math import get_random_int, nod

rules = 'Find the greatest common divisor of given numbers.'


def get_data():
    number1 = get_random_int()
    number2 = get_random_int()

    expression = '{0} {1}'.format(number1, number2)

    correct_answer = nod(number1, number2)

    return (expression, correct_answer)


def gcd():
    return game(rules, get_data)
