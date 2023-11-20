#!/usr/bin/env python3
from random import randint


def chech_if_even(num: int):
    if (num % 2 == 0):
        return True
    return False


def check_if_correct(answer: str, is_even: bool):
    if is_even is True and answer == 'yes':
        return True
    if is_even is False and answer == 'no':
        return True
    return False


def get_correct_answer(is_even: str):
    if is_even is True:
        return 'yes'
    return 'no'


def get_even_game():
    gameRule = 'Answer "yes" if the number is even, otherwise answer "no".'

    def gameLogic():
        question = randint(1, 100)
        is_even = chech_if_even(question)
        correctAnswer = get_correct_answer(is_even)
        return [question, correctAnswer]
    return [gameLogic, gameRule]
