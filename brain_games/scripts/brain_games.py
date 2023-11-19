#!/usr/bin/env python3
import prompt

def print_bg():
    print('brain-games')

def print_hello():
    print('Welcome to the Brain Games!')

def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ', name)

def main():
    print_bg()
    print_hello()
    welcome_user()

if __name__ == '__main__':
    main()