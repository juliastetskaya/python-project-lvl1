from brain_games.game import start_game
from brain_games.games.progression import RULES, get_game_data


def main():
    start_game(RULES, get_game_data)


if __name__ == '__main__':
    main()
