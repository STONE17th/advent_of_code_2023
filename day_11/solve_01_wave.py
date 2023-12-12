def data_reader(path: str) -> list[str]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    return data


class Cell:
    def __init__(self, row: int, index: int, number: int = 0, planet: bool = False):
        self.row = row
        self.index = index
        self.number = number
        self.is_planet = planet
        self.path = 0

    def __repr__(self):
        # return f'{self.path:^5}' if self.is_planet else f'{".":^5}'
        return f'{self.path:^5}'

    def __str__(self):
        return str(self.path)


class Galaxy:
    def __init__(self, path: str):
        self.map = data_reader(path)
        self._check_void()
        self.map = list(zip(*self.map))
        self._check_void()
        self.map = list(zip(*self.map))
        self.space = self.make_space()
        self.planets = self.make_planets()

    def make_space(self):
        space = []
        count = 1
        for i in range(len(self.map)):
            row = []
            for j in range(len(self.map[i])):
                if self.map[i][j] == '#':
                    row.append(Cell(i, j, count, True))
                    count += 1
                else:
                    row.append(Cell(i, j))
            space.append(row)
        return space

    def make_planets(self):
        planets = []
        for row in self.space:
            for cell in row:
                if cell.is_planet:
                    planets.append(cell)
        return planets

    def reset_paths(self):
        for i in range(len(self.space)):
            for k in range(len(self.space[i])):
                self.space[i][k].path = 0

    @property
    def paths(self):
        paths = []
        for i in range(len(self.planets)):
            for k in range(i + 1, len(self.planets)):
                paths.append((self.planets[i], self.planets[k]))
        return paths

    def _check_void(self):
        i = 0
        while i < len(self.map):
            if '#' not in self.map[i]:
                for _ in range(999999):
                    self.map.insert(i, self.map[i])
                i += 1000000
            else:
                i += 1

    def show(self):
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in self.space]))


def check_around(galaxy: Galaxy, cell: Cell) -> list[Cell]:
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cells = []
    for row, index in moves:
        x = cell.row + row
        y = cell.index + index
        if (0 <= x < len(galaxy.space)) and (0 <= y < len(galaxy.space[cell.row])) and galaxy.space[x][y].path == 0:
            galaxy.space[x][y].path = cell.path + 1
            cells.append(galaxy.space[x][y])
    return cells


def wave(galaxy: Galaxy, planet: Cell) -> int:
    wave_stack = check_around(galaxy, planet)
    while wave_stack:
        current_planet = wave_stack.pop(0)
        wave_stack += check_around(galaxy, current_planet)



def solution(galaxy: Galaxy) -> int:
    result = 0
    for planet in galaxy.planets:
        wave(galaxy, planet)
        for start, finish in galaxy.paths:
            if start == planet:
                result += finish.path
        galaxy.reset_paths()
    return result


data = Galaxy('test_data.txt')
print(len(data.planets))
print(solution(data))

