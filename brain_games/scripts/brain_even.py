#!/usr/bin/env python3
import prompt
from random import randint
from brain_games import utils


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


def even_game(user_name: str):
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    currentGameCounter = 0
    totalGamesCounter = 3
    print(rule)
    while currentGameCounter < totalGamesCounter:
        print(currentGameCounter)
        question = randint(1, 100)
        is_even = chech_if_even(question)
        print('Question: ', question)
        answer = prompt.string('Your answer: ')
        is_correct = check_if_correct(answer, is_even)
        if is_correct is False:
            text = 'is wrong answer ;(. Correct answer was'
            correctAnswer = get_correct_answer(is_even)
            res = f"'{answer}' {text} '{correctAnswer}'"
            print(res)
            print(f"Let's try again, {user_name}!")
            return
        if is_correct is True:
            print('Correct!')
            currentGameCounter = currentGameCounter + 1
    print(f'Congratulations, {user_name}!')


def main():
    user_name = utils.get_user_name()
    utils.print_bg()
    utils.print_hello()
    utils.welcome_user(user_name)
    even_game(user_name)


if __name__ == '__main__':
    main()
