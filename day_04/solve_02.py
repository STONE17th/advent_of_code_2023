def data_reader(path: str) -> dict[int, list]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    result = {}
    for i in range(len(data)):
        card, numbers = int(data[i].split(': ')[0].split()[1]), data[i].split(': ')[1].split(' | ')
        result[card] = (list(map(int, numbers[0].split())), list(map(int, numbers[1].split())))
    print(len(result))
    return result


WIN_SCORES = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


def check_win(ticket: list[tuple]) -> int:
    count = 0
    for number in ticket[0]:
        if number in ticket[1]:
            count += 1
    return count


def lottery_plunk(tickets: dict[list]):
    win_numbers = sorted(list(tickets), reverse=True)
    ticket_count = 0
    while win_numbers:
        ticket = int(win_numbers.pop())
        count = check_win(tickets.get(ticket))
        for shift in range(1, count + 1):
            win_numbers.insert(ticket, ticket + shift)
        ticket_count += 1
        print(ticket_count, len(win_numbers))
    return ticket_count


tickets_data = data_reader('input_data.txt')
print(lottery_plunk(tickets_data))
