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


def check_digit(list_of_digits):
    odd_digits = sum([int(x) for i, x in enumerate(list_of_digits)
                      if (i + 1) % 2 != 0])
    sum_of_all = (
        (odd_digits * 3) +
        sum([int(x) for i, x in enumerate(list_of_digits) if (i + 1) % 2 == 0])
    )
    mod_ten = sum_of_all % 10
    if mod_ten > 0:
        final_answer = 10 - mod_ten
    else:
        final_answer = mod_ten
    return final_answer


def main():
    all_upcs = mass_input(lines=int(input()))
    for upc in all_upcs:
        upc_digits_list = upc.split(' ')
        print(upc, check_digit(upc_digits_list))


if __name__ == '__main__':
    main()
