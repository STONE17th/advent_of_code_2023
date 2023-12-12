def data_reader(path: str) -> tuple[str, dict[str, tuple[str, str]]]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    path_data = data[0].replace('L', '0').replace('R', '1')
    result_map = {}
    for i in range(2, len(data)):
        key, value = data[i].split(' = ')
        result_map[key] = tuple(value.replace('(', '').replace(')', '').replace(',', '').split())
    return path_data, result_map


# 19185263738116
def solution(puzzle_data: tuple[str, dict[str, tuple[str, str]]]) -> int:
    data_path, data_map = puzzle_data
    my_place = [point for point in data_map if point.endswith('A')]
    turn = 0
    cycle_finish = [0]*len(my_place)
    while not all(map(lambda x: x != 0, cycle_finish)):
        for k in range(len(my_place)):
            my_place[k] = data_map.get(my_place[k])[int(data_path[turn % len(data_path)])]
            if my_place[k].endswith('Z') and not cycle_finish[k]:
                cycle_finish[k] = turn
        turn += 1
    total = 1
    for position in cycle_finish:
        cur = (position - 1) // len(data_path) + 1
        total *= cur
    return total * len(data_path)


data = data_reader('input_data.txt')
print(solution(data))
