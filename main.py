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
    my_place = [point for point in data_map if point.endswith('A')]
    start_point = my_place[0]
    turn = 1
    my_place[0] = data_map.get(my_place[0])[int(data_path[turn % len(data_path)])]
    while my_place[0] != start_point:
        # for k in range(len(my_place)):
        my_place[0] = data_map.get(my_place[0])[int(data_path[turn % len(data_path)])]
        turn += 1
        # if len(list(filter(lambda x: x.endswith('Z'), my_place))) >= 3:
        print(turn, my_place)
    print(my_place)
    return turn


data = data_reader('day_08/input_data.txt')
print(solution(data))
