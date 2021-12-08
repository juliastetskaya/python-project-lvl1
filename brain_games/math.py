from random import randint

from .constants import OPERATIONS, END_NUMBER, START_NUMBER, START_OPERATION_NUMBER, END_OPERATION_NUMBER

def is_even(num):
    return num % 2 == 0


def get_random_int():
    return randint(START_NUMBER, END_NUMBER)


def get_random_operation():
    random_number = randint(START_OPERATION_NUMBER, END_OPERATION_NUMBER)
    return OPERATIONS[random_number]


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b
