import re
from itertools import product


def data_reader(path: str) -> list[tuple[str, list[int]]]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip().split(), file.readlines()))
    result = []
    for i in range(len(data)):
        left = data[i][0].replace('.', '1').replace('#', '0').replace('?', 'x')
        right = list(map(lambda x: int(x), data[i][1].split(',')))
        result.append((left, right))
    return result


def solution(input_data: list[tuple[str, list[int]]]) -> int:
    result = 0
    for pattern, value in input_data:
        count = 0
        combos = list(product('01', repeat=pattern.count('x')))
        all_combos = []
        for combo in combos:
            i = 0
            example = ''
            for ch in pattern:
                if ch != 'x':
                    example += ch
                else:
                    example += str(combo[i])
                    i += 1
            all_combos.append(example)
        re_pattern = []
        for digit in value:
            re_pattern.append('[0]' + '{' + str(digit) + '}')
        re_pattern = '[1]*' + '[1]+'.join(re_pattern) + '[1]*'

        for row in all_combos:
            alignment = list(re.findall(re_pattern, row))
            if alignment:
                for a in alignment:
                    if len(a) == len(pattern):
                        count += 1
        result += count
    return result


data = data_reader('input_data.txt')
print(solution(data))
