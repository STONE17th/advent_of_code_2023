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
    input_seeds = data.get(0)
    print(input_seeds)
    minimal_dist = float('inf')
    for i in range(0, len(input_seeds) - 1, 2):
        for seed in range(input_seeds[i], input_seeds[i] + input_seeds[i+1]):
            for stage in range(1, len(data)):
                for seed_set in data.get(stage):

                    start, start_2, freq = seed_set
                    if start_2 <= seed and seed < start_2 + freq:
                        if start > start_2:
                            seed += start - start_2
                            break
                        else:
                            seed -= start_2 - start
                            break
            if seed < minimal_dist:
                minimal_dist = seed
    return minimal_dist


print(solution(seeds_data))
