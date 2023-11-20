#!/usr/bin/env python3
from random import randint


def getSumAndOperation(numberOfOperand, left, right):
    if numberOfOperand == 0:  # *
        return [left * right, '*']
    if numberOfOperand == 1:  # +
        return [left + right, '+']
    return [left - right, '-']  # default -


def get_calc_game():
    rule = 'What is the result of the expression?'

    def getLogic():
        left = randint(0, 25)
        right = randint(0, 25)
        [correctAns, operation] = getSumAndOperation(randint(0, 2), left, right)
        question = f'{left} {operation} {right}'
        return [question, f'{correctAns}']
    return [getLogic, rule]
