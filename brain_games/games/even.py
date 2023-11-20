#!/usr/bin/env python3
from random import randint


def chech_if_even(num: int):
    if (num % 2 == 0):
        return True
    return False


def get_correct_answer(is_even: str):
    if is_even is True:
        return 'yes'
    return 'no'


def get_even_game():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'

    def getLogic():
        question = randint(1, 100)
        is_even = chech_if_even(question)
        correctAnswer = get_correct_answer(is_even)
        return [question, correctAnswer]
    return [getLogic, rule]
