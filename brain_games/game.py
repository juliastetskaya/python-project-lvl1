import prompt
from brain_games.constants import MAX_GAMES_COUNT


def play(get_data, count=MAX_GAMES_COUNT):
    if count == 0:
        return True

    expression, correct_answer = get_data()

    print('Question: {0}'.format(expression))
    user_answer = prompt.string('Your answer: ')

    if user_answer == correct_answer:
        print('Correct!')
        return play(get_data, count - 1)

    template = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
    print(template.format(user_answer, correct_answer))

    return False


def game(rules, get_data):
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n{1}'.format(name, rules))

    text = 'Congratulations' if play(get_data) else "Let's try again"

    print('{0}, {1}!'.format(text, name))
