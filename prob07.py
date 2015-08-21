ACROPHONIC = [
    (50000, 'PM'),
    (10000, 'M'),
    (5000, 'PC'),
    (1000, 'C'),
    (500, 'PH'),
    (100, 'H'),
    (50, 'PD'),
    (10, 'D'),
    (5, 'PI'),
    (1, 'I')
]


def mass_input(lines=None, end=None):
    list_of_input = []
    if lines is not None:
        for x in range(lines):
            list_of_input.append(input())
    else:
        if end is None:
            end = ''
        i = input()
        while i != end:
            list_of_input.append(i)
            i = input()
    return list_of_input


def convert_to_acro(n):
    output = ''
    i = 0
    while n >= 1:
        dec_num = ACROPHONIC[i][0]
        acro_num = ACROPHONIC[i][1]
        if n >= dec_num:
            output += acro_num
            n -= dec_num
        else:
            i += 1
    return output


def convert_to_dec(string):
    # Assert every character in the string is in at least one acrophonic pair
    assert all([any([char in acro_str for acro_str in [pair[1] for pair in ACROPHONIC]]) for char in string])
    output = 0
    i = 0
    while len(string) > 0:
        dec_num = ACROPHONIC[i][0]
        acro_num = ACROPHONIC[i][1]
        if string == acro_num:
            output += dec_num
            break
        elif len(string) >= len(acro_num):
            if string[:len(acro_num)] == acro_num:
                output += dec_num
                string = string[len(acro_num):]
        else:
            i += 1
    return output


def main():
    all_nums = mass_input(lines=int(input()))
    for num in all_nums:
        try:
            num = int(num)
            print(convert_to_acro(num))
        except ValueError:
            print(convert_to_dec(num))


if __name__ == '__main__':
    main()
