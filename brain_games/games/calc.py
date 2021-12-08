from random import randint

import prompt
from brain_games.constants import END_NUMBER, MAX_GAMES_COUNT, START_NUMBER, OPERATIONS
from brain_games.math import get_random_operation, add, multiply, subtract

rules = 'What is the result of the expression?'


def play(name, count=MAX_GAMES_COUNT):
    if count == 0:
        print('Congratulations, {0}!'.format(name))
        return

    operand1 = randint(START_NUMBER, END_NUMBER)
    operand2 = randint(START_NUMBER, END_NUMBER)
    operation = get_random_operation()

    operations = {
        OPERATIONS[0]: add(operand1, operand2),
        OPERATIONS[1]: subtract(operand1, operand2),
        OPERATIONS[2]: multiply(operand1, operand2),
    }

    correct_answer = '{0}'.format(operations[operation])

    print('Question: {0} {1} {2}'.format(operand1, operation, operand2))
    user_answer = prompt.string('Your answer: ')

    if user_answer == correct_answer:
        print('Correct!')
        play(name, count - 1)
    else:
        template = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
        print(template.format(user_answer, correct_answer))
        print("Let's try again, {0}!".format(name))


def calc():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    print(rules)

    return play(name)
