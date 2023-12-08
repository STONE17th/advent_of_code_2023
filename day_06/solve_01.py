def data_reader(path: str) -> list[tuple[int, int]]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    data = [list(map(int, row.split()[1:])) for row in data]
    print(data)
    input_data = []
    for i in range(len(data[0])):
        input_data.append((data[0][i], data[1][i]))
    return input_data


def solution(data: list[tuple[int, int]]) -> int:
    result = 1
    for time, distance in data:
        count = 0
        for speed in range(1, time):
            if speed * (time - speed) > distance:
                count += 1
        print(count)
        result *= count
    return result


input_data = data_reader('input_data.txt')
print(input_data)
print(solution(input_data))
