CUBE_SET = {'red': 12,
            'green': 13,
            'blue': 14}


def data_reader(path: str) -> dict:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip().split(': '), file.readlines()))
    result = {}
    for row in data:
        cube_list = []
        for moves in row[1].split('; '):
            dict_cube = {}
            for cube in moves.split(','):
                count, color = cube.strip().split()
                dict_cube[color] = int(count)
            cube_list.append(dict_cube)
        result[int(row[0].split()[-1])] = cube_list
    return result


def game_checker(data: dict[int, [list[dict[str, int]]]]) -> int:
    result = {}
    for g_id, cube_values in data.items():
        correct = True
        for cube in cube_values:
            for color, count in cube.items():
                if CUBE_SET[color] < count:
                    correct = False
                    break
        result[g_id] = correct

    return sum([key for key, value in result.items() if value])


if __name__ == '__main__':
    data = data_reader('input_data.txt')
    print(game_checker(data))
