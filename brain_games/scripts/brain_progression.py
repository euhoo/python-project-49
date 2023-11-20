#!/usr/bin/env python3
from brain_games import game_engine
from brain_games.games.progression import get_progression_game


def play():
    [gameLogic, gameRule] = get_progression_game()
    game_engine.play(gameLogic, gameRule)


def main():
    play()


if __name__ == '__main__':
    main()
