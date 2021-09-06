"""Prompt and verify user input on the command line."""
import prompt


def welcome_user():
    """Greet user and request his/her name."""
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
