from random import choice, randint

RULES = 'What is the result of the expression?'
OPERATIONS = ('+', '-', '*')
START_NUMBER = 1
END_NUMBER = 10


def calculate(num1, num2, operation):
    operations = {
        OPERATIONS[0]: num1 + num2,
        OPERATIONS[1]: num1 - num2,
        OPERATIONS[2]: num1 * num2,
    }

    return str(operations[operation])


def get_game_data():
    operand1 = randint(START_NUMBER, END_NUMBER)
    operand2 = randint(START_NUMBER, END_NUMBER)
    operation = choice(OPERATIONS)

    expression = '{0} {1} {2}'.format(operand1, operation, operand2)

    correct_answer = calculate(operand1, operand2, operation)

    return (expression, correct_answer)
