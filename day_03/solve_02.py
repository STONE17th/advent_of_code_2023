def data_reader(path: str) -> list[str]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    return data


class Number:
    def __init__(self, row: int, index: int, star: tuple[int, int]):
        self.value = 0
        self.row = row
        self.anchor = index
        self.index = {index}
        self.star = star

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.row == other.row and self.index == other.index

    def __str__(self):
        return f'{self.value:<4} | {self.row:<4} x {str(self.index):<16} -> {str(self.star):<15}'

    def __repr__(self):
        return f'{self.value:<4} | {self.row:<4} x {str(self.index):<16} -> {self.star}'


def adjacent_coords(matrix: list[str], coords: tuple[int, int]) -> list[Number]:
    x, y = coords
    a_coords = []
    for k in [-1, 0, 1]:
        for n in [-1, 0, 1]:
            cur_x, cur_y = x + k if (0 <= x + k < len(matrix)) else None, y + n if (
                    0 <= y + n < len(matrix[x])) else None
            if not (cur_x is None or cur_y is None):
                if (k != 0 or n != 0) and matrix[cur_x][cur_y].isdigit():
                    if not a_coords or (
                            a_coords and not (a_coords[-1].row == cur_x and a_coords[-1].anchor == cur_y - 1)):
                        a_coords.append(Number(cur_x, cur_y, (x, y)))
    return a_coords


def collect_coords(matrix: list[str]) -> list[Number]:
    coordinates = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '*':
                list_nums = adjacent_coords(matrix, (i, j))
                # if len(list_nums) == 2:
                coordinates += list_nums
    return coordinates


def check_number(cell: Number, matrix: list[str]) -> int:
    x, y = cell.row, cell.anchor
    number = matrix[x][y]

    def turn(num: int):
        nonlocal number
        i = num
        while True:
            if 0 <= y + i < len(matrix[x]) and matrix[x][y + i].isdigit():
                if num == 1:
                    number += matrix[x][y + i]
                    cell.index.add(y + i)
                else:
                    number = matrix[x][y + i] + number
                cell.index.add(y + i)
                i += num
            else:
                break

    turn(1)
    turn(-1)
    cell.value = number
    return int(number)


def sum_matrix(nums: list[Number], matrix: [list[str]]) -> dict:
    result = []
    total = {}
    for num in nums:
        check_number(num, matrix)
        if num not in result:
            result.append(num)
    result = sorted(result, key=lambda x: x.star)
    [print(num) for num in result]
    for num in result:
        if total.get(num.star):
            total[num.star].append(int(num.value))
        else:
            total[num.star] = [int(num.value)]
    return total


input_matrix = data_reader('input_data.txt')

input_coords = collect_coords(input_matrix)
total = []
for key, value in sum_matrix(input_coords, input_matrix).items():
    mult = 1
    if len(value) == 2:
        for item in value:
            mult *= item
        total.append(mult)
print(sum(total))
