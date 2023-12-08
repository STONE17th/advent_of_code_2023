def data_reader(path: str) -> dict[int, list[list]]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    result = {0: list(map(int, data[0].split(':')[1].split()))}
    key = 0
    for row in data[1:]:
        if not row:
            continue
        if not row.replace(' ', '').isdigit():
            key += 1
            continue
        current_row = list(map(int, row.split()))
        if key in result:
            result[key].append(current_row)
        else:
            result[key] = [current_row]
    return result


seeds_data = data_reader('input_data.txt')


def solution(data: dict[int, [list[list]]]) -> int:
    seeds = data.get(0)
    print(seeds)
    for stage in range(1, len(data)):
        print('----------------')
        for i in range(len(seeds)):
            for seed_set in data.get(stage):

                start, start_2, freq = seed_set
                if start_2 <= seeds[i] and seeds[i] < start_2 + freq:
                    print(start, start_2, freq)
                    if start > start_2:
                        seeds[i] += start - start_2
                        break
                    else:
                        seeds[i] -= start_2 - start
                        break
            print(seeds)
    return min(seeds)


print(solution(seeds_data))
