SINGLE_SEGMENT = 15
DIVIDER = 20
MILLIAMPS = {
    ':': DIVIDER,
    '1': SINGLE_SEGMENT * 2,
    '2': SINGLE_SEGMENT * 5,
    '3': SINGLE_SEGMENT * 5,
    '4': SINGLE_SEGMENT * 4,
    '5': SINGLE_SEGMENT * 5,
    '6': SINGLE_SEGMENT * 6,
    '7': SINGLE_SEGMENT * 3,
    '8': SINGLE_SEGMENT * 7,
    '9': SINGLE_SEGMENT * 6,
    '0': SINGLE_SEGMENT * 6,
}


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


def main():
    all_times = mass_input(lines=int(input()))
    for time in all_times:
        print(sum([MILLIAMPS[char] for char in time]), 'milliamps')

if __name__ == '__main__':
    main()
