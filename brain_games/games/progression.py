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


def makeRow(first, step, correctAnswerIndex, progressionLength):
    row = ''
    currentIndex = 0
    while currentIndex <= progressionLength - 1:
        if currentIndex == correctAnswerIndex:
            row = f'{row} ..'
        else:
            row = f'{row} {first + (step * currentIndex)}'
        currentIndex = currentIndex + 1
    return row


def get_progression_game():
    rule = 'What number is missing in the progression?'
    progressionLength = 10

    def getLogic():
        first = randint(1, 10)
        step = randint(1, 15)
        correctAnsIndex = randint(0, progressionLength - 1)
        correctAnswer = first + (step * correctAnsIndex)
        question = makeRow(first, step, correctAnsIndex, progressionLength)
        return [question, f'{correctAnswer}']
    return [getLogic, rule]
