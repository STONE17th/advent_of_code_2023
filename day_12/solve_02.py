import re
from itertools import product

result = 0


def data_reader(path: str) -> list[tuple[str, list[int]]]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip().split(), file.readlines()))
    result_list = []
    for i in range(len(data)):
        left = data[i][0].replace('.', '1').replace('#', '0').replace('?', 'x')
        right = list(map(lambda x: int(x), data[i][1].split(',')))
        result_list.append((left, right))
    return result_list


def solution(input_data: list[tuple[str, list[int]]]) -> int:
    result = 0
    shift = 6
    step = 0
    for x_digit, pattern in input_data:
        step += 1
        main_pattern = '[1]+'.join(['[0]' + '{' + str(digit) + '}' for digit in pattern])
        start_of_lines = ['']
        for i in range(1, shift):
            pattern = '[1]*' + '[1]+'.join([main_pattern] * i) + '[1]*'
            new_lines = []
            while start_of_lines:
                line = start_of_lines.pop()
                if x_digit.endswith('1'):
                    line = ('x'.join([line, x_digit])) if line else x_digit
                else:
                    line = (''.join([line, x_digit]) if line else x_digit) + ('x' if i < (shift - 1) else '')

                for combo in list(product('01', repeat=line.count('x'))):
                    k = 0
                    new_line = ''
                    for ch in line:
                        if ch != 'x':
                            new_line += ch
                        else:
                            new_line += str(combo[k])
                            k += 1
                    alignment = re.fullmatch(pattern, new_line)
                    if alignment:
                        new_lines.append(new_line)
            start_of_lines = new_lines.copy()
        print(step, ' -> ', len(start_of_lines))
        result += len(start_of_lines)
    return result


data = data_reader('input_data.txt')
print(solution(data))
