from brain_games.game import game
from brain_games.math import get_random_index, get_random_int, make_progression

rules = 'What number is missing in the progression?'


def get_data():
    start = get_random_int()
    step = get_random_int()

    progression = make_progression([start], step)

    index = get_random_index()
    correct_answer = str(progression[index])
    progression[index] = '..'

    expression = ' '.join(str(num) for num in progression)

    return (expression, correct_answer)


def progression():
    return game(rules, get_data)
