from random import choice, randint

from brain_games.constants import (
    END_NUMBER,
    OPERATIONS,
    PROGRESSION_LENGTH,
    START_NUMBER,
)


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


def nod(num1, num2):
    if num1 % num2 == 0:
        return str(num2)

    return nod(num2, num1 % num2)


def make_progression(number_list, step, count=1):
    if count == PROGRESSION_LENGTH:
        return number_list

    number_list.append(number_list[-1] + step)
    return make_progression(number_list, step, count + 1)


def get_random_index():
    return randint(START_NUMBER + 1, END_NUMBER - 1)
