from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_NUMBER = 2
END_NUMBER = 100


def find_divisor(num, test_divisor):
    if test_divisor ** 2 > num:
        return num
    if num % test_divisor == 0:
        return test_divisor
    return find_divisor(num, test_divisor + 1)


def smallest_divisor(num):
    return find_divisor(num, 2)


def is_prime(num):
    return num == smallest_divisor(num)


def get_game_data():
    number = randint(START_NUMBER, END_NUMBER)

    correct_answer = 'yes' if is_prime(number) else 'no'

    return (number, correct_answer)
