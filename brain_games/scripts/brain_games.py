#!/usr/bin/env python3
import prompt


def print_bg():
    print('brain-games')


def print_hello():
    print('Welcome to the Brain Games!')


def get_user_name():
    return prompt.string('May I have your name? ')


def welcome_user(name: str):
    print('Hello, ', name)


def main():
    user_name = get_user_name()
    print_bg()
    print_hello()
    welcome_user(user_name)


if __name__ == '__main__':
    main()
