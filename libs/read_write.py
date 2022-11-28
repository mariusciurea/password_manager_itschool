"""read from file and write to file"""


def read_from_file(file_path):
    """
    returns the file content as a list
    every row within the file being a list element
    :param file_path:
    :return:
    """
    try:
        with open(file_path, 'r') as fr:
            content = fr.readlines()
        return content
    except FileNotFoundError as e:
        print(f'Fisierul nu se gaseste sau nu a putut fi deschis. '
              f'Eroarea: {e}')
        return
    except Exception as e:
        print(f'eroare neasteptata: -> {e}')
        return


def write_to_file(file_path, message):
    """
    append the message to the specified file
    :param file_path:
    :return:
    """
    try:
        with open(file_path, 'a+') as fw:
            fw.write(f'\n{message}')
        return True
    except OSError as e:
        print('probleme cu fisierul')
        return False
    except Exception as e:
        print(f'a aparut aceasta exceptie: -> {e}')
        return False


if __name__ == '__main__':

    names = read_from_file('nume.txt')
    if names:
        new_names = [name.strip() for name in names]
        # print(new_names)
        count = {item: new_names.count(item) for item in set(new_names)}
        print(count)
        if write_to_file('nume.txt', f'numarul de aparitii: {count}'):
            print('Am scris cu succes datele in fisier')
        else:
            print('datele nu pot fi scrise')
    else:
        print('eroare de fisier')
