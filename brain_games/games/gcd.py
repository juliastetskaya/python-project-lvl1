from random import randint

RULES = 'Find the greatest common divisor of given numbers.'
START_NUMBER = 1
END_NUMBER = 100


def gcd(num1, num2):
    if num1 % num2 == 0:
        return str(num2)

    return gcd(num2, num1 % num2)


def get_game_data():
    number1 = randint(START_NUMBER, END_NUMBER)
    number2 = randint(START_NUMBER, END_NUMBER)

    expression = '{0} {1}'.format(number1, number2)

    correct_answer = gcd(number1, number2)

    return (expression, correct_answer)
