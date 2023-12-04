def data_reader(path: str) -> list[str]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    return data


test_matrix = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.split('\n')

input_matrix = data_reader('input_data.txt')


def collect_coords(matrix: list[str]) -> list[tuple[int, int]]:
    coordinates = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] not in '1234567890.':
                for k in [-1, 0, 1]:
                    for n in [-1, 0, 1]:
                        if (k != 0 or n != 0) and matrix[i + k][j+n].isdigit():
                            coordinates.append((i + k, j + n))
    print(sorted(coordinates))
    new_coordinates = [coordinates[0]]
    i = 0
    while i < len(coordinates) - 1:
        s = 1
        while i + s  < len(coordinates) - 1:
            if coordinates[i+s] == (coordinates[i][0], coordinates[i][1] + s):
                s += 1
            else:
                new_coordinates.append(coordinates[i+s])
                i = i + s
                break
        i += 1
    return coordinates

# def alter_coords(matrix: list[str]) -> list[tuple[int,int]]:
#     alter_result = []
#     for x in range(len(matrix)):
#         for y in range(len(matrix[x])):
#             if matrix[x][y].isdigit():


def check_number(coord: tuple[int, int], matrix: list[str]) -> int:
    number = matrix[coord[0]][coord[1]]

    def turn(num: int):
        nonlocal number
        i = num
        while True:
            if coord[1] + i < len(matrix[coord[0]]) and matrix[coord[0]][coord[1] + i].isdigit():
                if num == 1:
                    number += matrix[coord[0]][coord[1] + i]
                else:
                    number = matrix[coord[0]][coord[1] + i] + number
                i += num
            else:
                break
    if number.isdigit():
        turn(1)
        turn(-1)
    return number


test_coords = collect_coords(test_matrix)
input_coords = collect_coords(input_matrix)


def sum_matrix(coords: list[tuple[int, int]], matrix: [list[str]]) -> int:
    result = []
    for coord in coords:
        number = int(check_number(coord, matrix))
        # if matrix[coord[0]][coord[1]].isdigit():
        #     number = int(check_number(coord, matrix))
        #     if len(result) < 2:
        #         result.append(number)
        #     if len(result) > 1 and result[-1] != number:
        result.append(number)
    return sum(result)


print(sum_matrix(test_coords, test_matrix))
print(sum_matrix(input_coords, input_matrix))
