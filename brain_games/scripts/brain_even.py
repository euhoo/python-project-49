#!/usr/bin/env python3
import prompt
from random import randint

def print_bg():
    print('brain-games')


def print_hello():
    print('Welcome to the Brain Games!')


def get_user_name():
    return prompt.string('May I have your name? ')


def welcome_user(name: str):
    print('Hello, ', name)


def play_game(rule: str, question: str, answer: str):
    print(rule)


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
    user_name = get_user_name()
    print_bg()
    print_hello()
    welcome_user(user_name)
    even_game(user_name)


if __name__ == '__main__':
    main()
