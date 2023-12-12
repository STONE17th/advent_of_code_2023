class Cell:
    samples = {'F': ((1, 0), (0, 1)),
               '7': ((0, -1), (1, 0)),
               'J': ((0, -1), (-1, 0)),
               'L': ((0, 1), (-1, 0)),
               '-': ((0, -1), (0, 1)),
               '|': ((-1, 0), (1, 0))}

    def __init__(self, row: int, index: int, value: str):
        self.row = row
        self.index = index
        self.value = value
        self.path = 0

    def __repr__(self):
        return str(self.value)


class Puzzle:
    def __init__(self, data_map: list[list[Cell]]):
        self.map = data_map
        self.movement_list = []
        self.counter = 0

    @property
    def start_coords(self) -> tuple[int, int]:
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if self.map[x][y].value == 'S':
                    return x, y

    def solve(self):
        cur_x, cur_y = self.start_coords
        start_list = []
        start_coord = {(1, 0): '|LJ', (-1, 0): '|F7', (0, 1): '-J7', (0, -1): '-FL'}
        for coord, values in start_coord.items():
            x, y = cur_x + coord[0], cur_y + coord[1]
            if self.map[x][y].value in values:
                start_list.append(self.map[x][y])
        self.movement_list.append(start_list)
        while any(map(lambda x: len(x) > 0, self.movement_list)):
            current_list = self.movement_list.pop(0)
            self.counter += 1
            new_list = set()
            if current_list:
                for cell in current_list:
                    if cell.value in '7FL-J|' and cell.path == 0:
                        for coords in Cell.samples.get(cell.value):
                            if cell.value != 'S':
                                cell.path = self.counter
                            x, y = cell.row + coords[0], cell.index + coords[1]
                            if (self.map[x][y].value in '7FL-J|' and
                                    self.map[x][y].path == 0 and
                                    0 <= x < len(self.map) and
                                    0 <= y < len(self.map[x])):
                                new_list.add(self.map[x][y])
            self.movement_list.append(new_list)

    def show(self, path: bool = True):
        result = []
        for x in range(len(self.map)):
            row = []
            for y in range(len(self.map[x])):
                cell = self.map[x][y].path if path else self.map[x][y].value
                row.append(f'{cell:^6}')
            result.append(''.join(row))
        print('\n'.join(result))


def data_reader(path: str) -> list[list[Cell]]:
    result = []
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    for x in range(len(data)):
        row_list = []
        for y in range(len(data[x])):
            row_list.append(Cell(x, y, data[x][y]))
        result.append(row_list)
    return result


data_map = data_reader('input_data.txt')
puzzle = Puzzle(data_map)
print(puzzle.start_coords)
puzzle.show(False)
puzzle.solve()
puzzle.show(True)
print(puzzle.counter)

# 6815
