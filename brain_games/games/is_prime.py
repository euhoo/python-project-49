#!/usr/bin/env python3
from random import randint


def is_prime(num: int):
    smallestPrime = 2
    if (num < smallestPrime):
        return True
    current = smallestPrime
    while (current < num):
        if num % current == 0:
            return False
        current = current + 1
    return True


def get_str_answer_by_bool_answer(answer: bool):
    if (answer is True):
        return 'yes'
    return 'no'


def get_is_prime_game():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    def getLogic():
        question = randint(1, 25)
        correctBoolAnswer = is_prime(question)
        return [question, get_str_answer_by_bool_answer(correctBoolAnswer)]
    return [getLogic, rule]
