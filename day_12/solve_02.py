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
        true_right = []
        for _ in range(5):
            true_right += right
        result_list.append(('x'.join(left*5), true_right))
    return result_list


def solution(input_data: list[tuple[str, list[int]]]) -> int:
    result = 0
    for pattern, value in input_data:
        inputs = ['']
        re_pattern = []
        print(value)
        for digit in value:
            re_pattern.append('[0]' + '{' + str(digit) + '}')
            temp_pattern = '[1]*' + '[1]+'.join(re_pattern) + '[0-1]*'
            for combo in list(product('01', repeat=temp_pattern.count('x'))):
                i = 0
                for i in range(len(inputs)):
                    example = inputs.pop(i)
                    for ch in temp_pattern:
                        if ch != 'x':
                            example += ch
                        else:
                            example += str(combo[i])
                            i += 1
                    alignment = list(re.findall(temp_pattern, example))
                    print(temp_pattern, example)
                    if alignment:
                        for a in alignment:
                            if len(a) == len(pattern):
                                inputs.append(example)
        result += len(inputs)
    return result




data = data_reader('test_data.txt')
solution(data)
print(result)
