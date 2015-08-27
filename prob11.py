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


def get_remainders(n, divisors):
    return tuple(n % d for d in divisors)


def divisible_by_all(n, pairs):
    return all(n % pair[0] == pair[1] for pair in pairs)


def get_from_remainders(*pairs):
    pairs = list(pairs)
    pairs = sorted(pairs, key=lambda x: x[0])
    largest_divisor = pairs[-1][0]
    x = pairs[-1][1]
    if x == 0:
        x += largest_divisor
    while not divisible_by_all(x, pairs):
        x += largest_divisor
    return x


def main():
    all_input = mass_input(end='-1 -1 -1 -1 -1 -1')
    for i in all_input:
        a, b, c, x, y, z = (int(n) for n in i.split(' '))
        print(get_from_remainders((a, x), (b, y), (c, z)))

if __name__ == '__main__':
    main()
