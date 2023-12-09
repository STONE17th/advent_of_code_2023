import os
import sys


def create_base():
    for i in range(1, 26):
        path = f'day_{str(i).zfill(2)}'
        if not os.path.exists(path):
            os.mkdir(path)
            file_names = ['__init__.py', 'test_data.txt', 'input_data.txt',
                          'solve_01.py', 'solve_02.py']
            for name in file_names:
                with open(os.path.join(path, name), 'w', encoding='UTF-8') as file:
                    file.write('')


if __name__ == '__main__':
    create_base()
