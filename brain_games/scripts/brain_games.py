#!/usr/bin/env python3
from brain_games import utils


def main():
    user_name = utils.get_user_name()
    utils.welcome_user(user_name)


if __name__ == '__main__':
    main()
