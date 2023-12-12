def data_reader(path: str) -> dict[str, list[int]]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip().split(), file.readlines()))
    result = {}
    for i in range(len(data)):
        result[data[i][0]] = list(map(lambda x: '#' * int(x), data[i][1].split(',')))
    return result


def solution(input_data: dict[str, list[int]]) -> int:
    for pattern, value in input_data.items():
        pattern = ('.' if pattern.startswith('#') else '') + pattern + ('.' if pattern.endswith('#') else '')
        print(pattern, len(pattern), len('.'.join(value)), '.'.join(value))
        print(max(value, key=len))


data = data_reader('test_data.txt')
solution(data)


import re

pattern = r'[#?]{6}'

text = '#?#?.#?#?.???#.?#?##'

print(re.findall(pattern, text))