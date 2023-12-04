from solve_01 import data_reader

cube_data = data_reader('input_data.txt')


def power_of_cubes(data: dict[int, [list[dict[str, int]]]]) -> int:
    result = {}
    for g_id, cubes in data.items():
        cube_power = {'red': 0, 'green': 0, 'blue': 0}
        for cube in cubes:
            for color, count in cube.items():
                cube_power[color] = count if cube_power[color] < count else cube_power[color]
        result[g_id] = cube_power
    total = []
    for cube in result.values():
        power = 1
        for count in cube.values():
            power *= count
        total.append(power)
    return sum(total)


if __name__ == '__main__':
    print(power_of_cubes(cube_data))
