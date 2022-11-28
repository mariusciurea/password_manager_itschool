# inregistrare curs

"""
password manager
"""

from libs import read_write as rw
import random
import string


def menu() -> str:
    print(f'save account: [s]\n'
          f'exit [e]')
    option: str = input('your choise: ')
    return option


def account_menu():
    app = input("Enter a name of an app:")
    print("Do you want to use a randome password [r]\n"
          "or a manually generated password [m]")
    option = input("your option:")
    if option == "r":
        password = generate_random_pass()
    elif option == "m":
        password = input("write manually generated password:")

    return app, password


def generate_random_pass() -> str:
    p = random.sample(string.ascii_letters, 4) + random.sample(string.digits + string.punctuation, 6)
    password = ''.join(p)
    return password


if __name__ == '__main__':
    result = menu()

    while result != "e":
        if result == 's':
            app, passwd = account_menu()
            file_content: list = rw.read_from_file('apps.txt')
            for row in file_content:
                if app in row:
                    print('aplicatia deja exista!')
                    break
            else:
                rw.write_to_file('apps.txt', f'{app}:{passwd}\n')
        result = menu()
