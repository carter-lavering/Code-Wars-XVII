def mass_input(lines=None, end=None):
    """Takes multiple lines of input."""
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


def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def main():
    num_of_letters = int(input())
    letters = sorted(input().split(' '))
    assert len(letters) == num_of_letters
    indices = [int(num) for num in mass_input(end='0')]
    five_letter_words = sorted(list(set(
        ''.join(word) for word in permutations(letters, 5)
    )))
    for i in indices:
        print(i, five_letter_words[i - 1], sep=': ')
    # for word in five_letter_words:
    #     print(word)


if __name__ == '__main__':
    main()
