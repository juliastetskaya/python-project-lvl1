import prompt
from brain_games.constants import MAX_GAMES_COUNT
from brain_games.math import is_even, get_random_int

rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def play(name, count=MAX_GAMES_COUNT):
    if count == 0:
        print('Congratulations, {0}!'.format(name))
        return

    number = get_random_int()
    correct_answer = 'yes' if is_even(number) else 'no'

    print('Question: {0}'.format(number))
    user_answer = prompt.string('Your answer: ')

    if user_answer == correct_answer:
        print('Correct!')
        play(name, count - 1)
    else:
        template = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
        print(template.format(user_answer, correct_answer))
        print("Let's try again, {0}!".format(name))


def even():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    print(rules)

    return play(name)
