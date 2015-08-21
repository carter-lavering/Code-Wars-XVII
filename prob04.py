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
    count = int(input())
    raw_inputs = mass_input(lines=int(input()))
    split_inputs = [i.split(' ') for i in raw_inputs]
    all_names = [i[-1] for i in split_inputs]
    guesses = {i[-1]: int(i[0]) for i in split_inputs}
    differences = {name: abs(count - guesses[name]) for name in guesses}
    best_diff = 1000
    for name in all_names:
        if differences[name] < best_diff:
            best_diff = differences[name]
    print(' '.join([name for name in all_names if differences[name] == best_diff]))

if __name__ == '__main__':
    main()
