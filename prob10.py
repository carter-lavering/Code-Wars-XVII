def get_value(char):
    capital = char.upper()
    if capital in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(capital) + 1
    else:
        return 1


def encode(string):
    indexes_by_char = {}
    length = len(string)
    current_index = get_value(string[0])
    for char in string[1:]:
        pass


def main():
    pass


if __name__ == '__main__':
    main()
