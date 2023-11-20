#!/usr/bin/env python3
from brain_games import game_engine
from brain_games.games.even import get_even_game


def play_even():
    [gameLogic, gameRule] = get_even_game()
    game_engine.play(gameLogic, gameRule)


def main():
    play_even()


if __name__ == '__main__':
    play_even()
