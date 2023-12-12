def data_reader(path: str) -> list[str]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    return data


class Planet:
    def __init__(self, row: int, index: int, number: int):
        self.row = row
        self.index = index
        self.row_sized = row
        self.index_sized = index
        self.number = number

    def __repr__(self):
        return str((self.number, (self.row, self.index)))


class Galaxy:
    def __init__(self, data: list[str]):
        self.galaxy = data
        self.planets = self._collect_planets()
        self.paths = self._collect_paths()

    def _collect_planets(self):
        planets = []
        count = 1
        for i in range(len(self.galaxy)):
            for k in range(len(self.galaxy[i])):
                if self.galaxy[i][k] == '#':
                    planets.append(Planet(i, k, count))
                    count += 1
        return planets

    def _collect_paths(self):
        paths = []
        for i in range(len(self.planets)):
            for k in range(i + 1, len(self.planets)):
                paths.append((self.planets[i], self.planets[k]))
        return paths

    def sizing(self, scale: int):
        row_size = {}
        for i in range(len(self.galaxy)):
            if '#' not in self.galaxy[i]:
                for planet in self.planets:
                    if planet.row > i:
                        planet.row_sized += scale - 1
        self.galaxy = list(zip(*self.galaxy))
        for i in range(len(self.galaxy)):
            if '#' not in self.galaxy[i]:

                for planet in self.planets:
                    if planet.index > i:
                        planet.index_sized += scale - 1

    def total_paths(self):
        result = 0
        for path in self.paths:
            print(path, dist := self.distance(path))
            result += dist
        return result

    def distance(self, planets: tuple[Planet, Planet]) -> int:
        delta_row = abs(planets[1].row_sized - planets[0].row_sized)
        delta_index = abs(planets[0].index_sized - planets[1].index_sized)

        return delta_row + delta_index


data = data_reader('input_data.txt')
galaxy = Galaxy(data)
print(galaxy.total_paths())
galaxy.sizing(1000000)
print(galaxy.total_paths())

# 504706009068438
# 504715068438