def data_reader(path: str) -> list[list[str]]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    result = []
    mirror = []
    for row in data:
        if row:
            mirror.append(row)
        else:
            result.append(mirror)
            mirror = []
    else:
        result.append(mirror)
    return result


class Mirror:
    def __init__(self, data_mirror: list[str]):
        self.flat = data_mirror
        self.original = data_mirror.copy()
        self.clean = False

    def rotate(self):
        self.flat = list(map(lambda x: ''.join(x), zip(*self.flat)))
        print('ПОВОРОТ!!')

    def find_center(self):
        result = []
        for i in range(len(self.flat) - 1):
            if res := self.reflection(i):
                result.append(res)
        print(f'{result=}')
        return min(result) if result else 0

    def reflection(self, center: int):
        to_up, to_down = center, center + 1
        # if self.flat[to_up] != self.flat[to_down]:
        #     return False
        while 0 <= to_up and len(self.flat) > to_down:
            if self.flat[to_up] != self.flat[to_down]:
                if not self.clean:
                    self.clean = self.clean_smudge(to_up, to_down)
                    continue
                return False
            to_up -= 1
            to_down += 1
        return center + 1

    def clean_smudge(self, h_row: int, l_row: int):
        for i in range(len(self.flat[0])):
            if self.flat[h_row][i] != self.flat[l_row][i]:
                row = list(self.flat[h_row])
                row[i] = self.flat[l_row][i]
                self.flat[h_row] = ''.join(row)
                print(f'CLEAN!! {h_row} {i}')
                return True
        return False



    def __str__(self):
        result = []
        for row in self.flat:
            flat_row = []
            for ch in row:
                flat_row.append(f'{ch:^3}')
            result.append(''.join(flat_row))
        return '\n'.join(result)


def solution(mirrors_data: list[list[str]]):
    result = 0
    for num, mirror in enumerate(mirrors_data):
        mirror = Mirror(mirror)
        print(mirror)
        reflect = mirror.find_center()*100
        if reflect:
            result += reflect
        else:
            mirror.rotate()
            result += mirror.find_center()
        print(mirror)
        print()
    return result
    #     if not num % 2:
    #         mirror.rotate()
    #         result += mirror.find_center()
    #     else:
    #         result += mirror.find_center() * 100
    #     print(mirror)
    #     print()
    #     print(result)
    #     print()
    # return result


data = data_reader('test_data.txt')
print(solution(data))

nor = [False, 1, 4]
print(min(nor, key=lambda x: x > 0))