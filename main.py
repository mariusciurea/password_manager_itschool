# inregistrare curs

"""
password manager
"""

from libs import read_write


def menu() -> str:
    print(f'save account: [s]\n'
          f'exit [e]')
    option = input('your choise: ')
    return option


def account_menu():
    pass


def generate_random_pass():
    pass


if __name__ == '__main__':
    menu()