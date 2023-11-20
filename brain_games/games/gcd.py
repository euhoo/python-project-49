#!/usr/bin/env python3
from random import randint


def findGCD(num1: int, num2: int):
    res = 1
    min = num1
    if num1 > num2:
        min = num2

    while min >= 1:
        if num2 % min == 0 and num1 % min == 0:
            res = min
            return res
        min = min - 1
    return res


def get_gcd_game():
    rule = 'Find the greatest common divisor of given numbers.'

    def getLogic():
        left = randint(1, 25)
        right = randint(1, 25)
        correctAnswer = findGCD(left, right)
        print('correctAnswer', correctAnswer)

        question = f'{left} {right}'
        return [question, f'{correctAnswer}']
    return [getLogic, rule]
