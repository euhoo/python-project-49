import prompt



def print_hello():
    print('Welcome to the Brain Games!')


def get_user_name():
    return prompt.string('May I have your name? ')


def welcome_user(name: str):
    print(f'Hello, {name}!')
