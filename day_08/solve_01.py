def data_reader(path: str) -> tuple[str, dict[str, tuple[str, str]]]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    path_data = data[0].replace('L', '0').replace('R', '1')
    result_map = {}
    for i in range(2, len(data)):
        key, value = data[i].split(' = ')
        result_map[key] = tuple(value.replace('(', '').replace(')', '').replace(',', '').split())
    return path_data, result_map


def solution(puzzle_data: tuple[str, dict[str, tuple[str, str]]]) -> int:
    data_path, data_map = puzzle_data
    my_place = 'AAA'
    turn = 0
    while my_place != 'ZZZ':
        my_place = data_map.get(my_place)[int(data_path[turn % len(data_path)])]
        turn += 1
    return turn


data = data_reader('input_data.txt')
print(solution(data))
