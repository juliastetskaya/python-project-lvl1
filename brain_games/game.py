import prompt

MAX_GAMES_NUMBER = 3


def play(get_game_data, game_counter=MAX_GAMES_NUMBER):
    if game_counter == 0:
        return True

    expression, correct_answer = get_game_data()

    print('Question: {0}'.format(expression))
    user_answer = prompt.string('Your answer: ')

    if user_answer == correct_answer:
        print('Correct!')
        return play(get_game_data, game_counter - 1)

    template = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
    print(template.format(user_answer, correct_answer))

    return False


def start_game(rules, get_game_data):
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n{1}'.format(name, rules))

    text = 'Congratulations' if play(get_game_data) else "Let's try again"

    print('{0}, {1}!'.format(text, name))
