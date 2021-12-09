from brain_games.game import game
from brain_games.math import calculate, get_random_int, get_random_operation

rules = 'What is the result of the expression?'


def get_data():
    operand1 = get_random_int()
    operand2 = get_random_int()
    operation = get_random_operation()

    expression = '{0} {1} {2}'.format(operand1, operation, operand2)

    correct_answer = calculate(operand1, operand2, operation)

    return (expression, correct_answer)


def calc():
    return game(rules, get_data)
