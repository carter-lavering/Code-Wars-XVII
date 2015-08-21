NEGATIVES = ("DOIN'T CAN'T ISN'T HAVEN'T CANNOT WOULDN'T COULDN'T WON'T NO NOT"
             " NEVER NOBODY NOWHERE NEITHER AIN'T".split(' '))
PUNCTUATION = ',;:?!"'


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
    all_sentences = mass_input(end='.')
    for original_sentence in all_sentences:
        for p in PUNCTUATION:
            s = original_sentence.replace(p, '')
        negative_count = 0
        for word in s.split():
            if word in NEGATIVES:
                negative_count += 1
        print(negative_count, original_sentence, sep=': ')


if __name__ == '__main__':
    main()
