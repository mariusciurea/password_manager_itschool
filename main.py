# inregistrare curs

"""
password manager
"""
# test
from libs import read_write as rw
import random
import string


def menu() -> str:
    print(f'save account: [s]\n'
          f'exit [e]')
    option: str = input('your choise: ')
    return option


def account_menu():
    pass


def generate_random_pass() -> str:
    p = random.sample(string.ascii_letters, 4) + random.sample(string.digits + string.punctuation, 6)
    password = ''.join(p)
    return password


def test_funct():
    print('test')


if __name__ == '__main__':
    result = menu()
    print(result)
    if result == 's':
        app, passwd = account_menu()
        file_content: list = rw.read_from_file('apps.txt')
        for row in file_content:
            if app in row:
                print('aplicatia deja exista!')
                break
        else:
            rw.write_to_file('apps.txt', f'{app}:{passwd}')
