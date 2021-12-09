from random import choice, randint

from brain_games.constants import END_NUMBER, OPERATIONS, START_NUMBER


def is_even(num):
    return num % 2 == 0


def get_random_int():
    return randint(START_NUMBER, END_NUMBER)


def get_random_operation():
    return choice(OPERATIONS)


def add(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def subtract(num1, num2):
    return num1 - num2


def calculate(num1, num2, operation):
    operations = {
        OPERATIONS[0]: add(num1, num2),
        OPERATIONS[1]: subtract(num1, num2),
        OPERATIONS[2]: multiply(num1, num2),
    }

    return str(operations[operation])
