def data_reader(path: str) -> list[tuple]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    result = []
    for i in range(len(data)):
        data[i] = data[i].split(': ')[1].split(' | ')
        result.append((list(map(int, data[i][0].split())), list(map(int, data[i][1].split()))))
    return result


WIN_SCORES = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


def check_win(lottery_tickets: list) -> int:
    result = 0
    for ticket in lottery_tickets:
        count = 0
        for nums in ticket[0]:
            if nums in ticket[1]:
                count += 1
        result += WIN_SCORES[count]
    return result

tickets = data_reader('input_data.txt')
print(check_win(tickets))