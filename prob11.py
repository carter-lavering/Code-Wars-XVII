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


def get_from_remainders(divisors, remainders):
    x = 1
    assert len(divisors) == len(remainders)
    all_remainders_true = all(
        x % divisors[i] == remainders[i] for i in len(divisors)
    )
    while not all_remainders_true:
        x += 1
        all_remainders_true = all(
            x % divisors[i] == remainders[i] for i in len(divisors)
        )
    return x


def main():
    all_input = mass_input(end='-1 -1 -1 -1 -1 -1')
    for i in all_input:
        a, b, c, x, y, z = tuple(i.split(' '))
