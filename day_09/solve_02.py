def data_reader(path: str) -> list[list[int]]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: list(map(int, x.strip().split())), file.readlines()))
    return data


def solution(data: list[list[int]]) -> int:
    result = 0

    def check_difference(data_row: list[int]):
        nonlocal difference_list
        local_list = []
        for i in range(len(data_row) - 1):
            local_list.append(data_row[i + 1] - data_row[i])
        difference_list.append(local_list)
        if all(map(lambda x: x == 0, local_list)):
            return
        check_difference(local_list)

    for row in data:
        # print(row)
        difference_list = [row]
        check_difference(row)
        difference_list = difference_list[::-1]
        for k in range(len(difference_list) - 1):
            new_element = difference_list[k + 1][0] - difference_list[k][0]
            difference_list[k + 1].insert(0, new_element)
        result += difference_list[-1][0]
    return result


input_data = data_reader('input_data.txt')
print(solution(input_data))
