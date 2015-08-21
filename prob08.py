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
    for sentence in mass_input(end='0 $'):
        sentence = sentence.split(' ')[:-1]
        print(sentence[-int(sentence[0])])


if __name__ == '__main__':
    main()
