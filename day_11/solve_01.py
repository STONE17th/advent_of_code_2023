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