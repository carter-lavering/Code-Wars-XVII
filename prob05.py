ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


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
    all_input = mass_input(end='.')
    for phrase in all_input:
        letter_count = {letter: 0 for letter in ALPHABET}
        for letter in phrase:
            if letter in ALPHABET:
                letter_count[letter] += 1
        if all([letter_count[L] == 1 for L in ALPHABET]):
            phrase_type = 'PERFECT'
        elif not any([letter_count[L] == 0 for L in ALPHABET]):
            phrase_type = 'PANGRAM'
        else:
            phrase_type = 'NEITHER'
        print(phrase_type, phrase, sep=': ')


if __name__ == '__main__':
    main()
