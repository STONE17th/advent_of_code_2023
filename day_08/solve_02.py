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
    # my_place = [point for point in data_map if point.endswith('A')]
    my_place = ['BSZ', 'GCF', 'TRJ', 'STL', 'GJC', 'MMH']
    turn = 1002790137
    while not all(map(lambda x: x.endswith('Z'), my_place)):
        for k in range(len(my_place)):
            my_place[k] = data_map.get(my_place[k])[int(data_path[turn % len(data_path)])]
        turn += 1
        if len(list(filter(lambda x: x.endswith('Z'), my_place))) >= 3:
            print(turn, my_place)
    print(my_place)
    return turn


data = data_reader('input_data.txt')
print(solution(data))
