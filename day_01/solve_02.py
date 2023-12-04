def solution_code(path: str) -> int:
    STR_DIGIT = ['zero', 'one', 'two', 'three',
                 'four', 'five', 'six', 'seven',
                 'eight', 'nine']
    with open(path, 'r', encoding='UTF-8') as file:
        some_data = list(map(lambda x: x.strip(), file.readlines()))
    for i in range(len(some_data)):
        for k in range(len(some_data[i])):
            current_slice = some_data[i][k:k + 5]
            for n in range(len(STR_DIGIT)):
                if STR_DIGIT[n] in current_slice:
                    some_data[i] = some_data[i].replace(STR_DIGIT[n], str(n) + STR_DIGIT[n][-1:])
    result = []
    for row in some_data:
        digit_row = ''
        for ch in row:
            if ch.isdigit():
                digit_row += ch
        result.append(digit_row)
    for i in range(len(result)):
        result[i] = int(result[i][0] + result[i][-1])
    return sum(result)


if __name__ == '__main__':
    print(solution_code('input_data.txt'))
