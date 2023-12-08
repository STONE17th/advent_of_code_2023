def data_reader(path: str) -> list[int, int]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    data = list(map(int, [''.join([ch for ch in row if ch.isdigit()]) for row in data]))
    return data


def solution(data: list[int, int]) -> int:
    time, distance = data
    count = 0
    for speed in range(1, time):
        if speed * (time - speed) > distance:
            count += 1
    return count


input_data = data_reader('input_data.txt')
print(input_data)
print(solution(input_data))
