from random import randint

RULES = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10
START_NUMBER = 0
END_NUMBER = 20
START_INDEX = 1
END_INDEX = 9


def make_progression(number_list, step, count=1):
    if count == PROGRESSION_LENGTH:
        return number_list

    number_list.append(number_list[-1] + step)
    return make_progression(number_list, step, count + 1)


def get_game_data():
    start_number = randint(START_NUMBER, END_NUMBER)
    step = randint(START_NUMBER, END_NUMBER)

    progression = make_progression([start_number], step)

    index = randint(START_INDEX, END_INDEX)
    correct_answer = str(progression[index])
    progression[index] = '..'

    expression = ' '.join(str(num) for num in progression)

    return (expression, correct_answer)
