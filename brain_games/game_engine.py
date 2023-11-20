#!/usr/bin/env python3
from brain_games import utils
import prompt


def play(logicOfGame, ruleOfGame: str):
    user_name = utils.get_user_name()
    utils.print_bg()
    utils.print_hello()
    utils.welcome_user(user_name)
    print(ruleOfGame)
    currentGameCounter = 0
    totalGamesCounter = 3
    while currentGameCounter < totalGamesCounter:
        [question, correctAnswer] = logicOfGame()
        print('Question: ', question)
        answer = prompt.string('Your answer: ')
        if correctAnswer == answer:
            currentGameCounter = currentGameCounter + 1
        else:
            text = 'is wrong answer ;(. Correct answer was'
            print(f'{answer} {text} {correctAnswer}')
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
