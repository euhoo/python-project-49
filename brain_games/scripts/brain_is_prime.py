#!/usr/bin/env python3
from brain_games import game_engine
from brain_games.games.is_prime import get_is_prime_game


def play():
    [gameLogic, gameRule] = get_is_prime_game()
    game_engine.play(gameLogic, gameRule)


def main():
    play()


if __name__ == '__main__':
    main()
