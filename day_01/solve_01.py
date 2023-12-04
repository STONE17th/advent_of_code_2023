def calibrate_trebuchet(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    result = []
    for row in data:
        digit_row = ''
        for ch in row:
            if ch.isdigit():
                digit_row += ch
        result.append(digit_row)
    for i in range(len(result)):
        result[i] = int(result[i][0] + result[i][-1])
    return sum(result)


if __name__ == '__main__':
    print(calibrate_trebuchet('input_data.txt'))
