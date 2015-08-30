BANNER_ALPHABET = """..A..
.A.A.
.AAA.
A...A
A...A
BBBB.
B...B
BBBB.
B...B
BBBB.
.CCC.
C...C
C....
C...C
.CCC.
DDDD.
D...D
D...D
D...D
DDDD.
EEEEE
E....
EEEEE
E....
EEEEE
FFFFF
F....
FFFFF
F....
F....
.GGG.
G....
G.GGG
G...G
.GGG.
H...H
H...H
HHHHH
H...H
H...H
IIIII
..I..
..I..
..I..
IIIII
....J
....J
....J
J...J
.JJJ.
K...K
K..K.
KKK..
K..K.
K...K
L....
L....
L....
L....
LLLLL
M...M
MM.MM
M.M.M
M...M
M...M
N...N
NN..N
N.N.N
N..NN
N...N
.OOO.
O...O
O...O
O...O
.OOO.
PPPP.
P...P
PPPP.
P....
P....
.QQQ.
Q...Q
Q...Q
Q..QQ
.QQQQ
RRRR.
R...R
RRRR.
R..R.
R...R
.SSS.
S....
.SSS.
....S
.SSS.
TTTTT
..T..
..T..
..T..
..T..
U...U
U...U
U...U
U...U
.UUU.
V...V
V...V
V...V
.V.V.
..V..
W...W
W...W
W.W.W
W.W.W
.W.W.
X...X
.X.X.
..X..
.X.X.
X...X
Y...Y
.Y.Y.
..Y..
..Y..
..Y..
ZZZZZ
...Z.
..Z..
.Z...
ZZZZZ"""

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

LETTERS_DICT = {
    tuple(line.replace('.', ' ').replace(letter, '#')
          for line in BANNER_ALPHABET.split('\n') if letter in line):
    letter for letter in ALPHABET
}

SPACE = ('     ', '     ', '     ', '     ', '     ')
LETTERS_DICT[SPACE] = ' '


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


def multiline_reversed(string):
    return '\n'.join(''.join(reversed(line)) for line in string.split('\n'))


def split_banners(multiple_line_banner):
    """Splits multiple banners into a list."""
    return [banner.strip('\n')
            for banner in multiple_line_banner.split('\n\n')]


def split_banner(banner):
    """Splits a banner into letters."""
    banner_lines = banner.split('\n')
    # Make sure every line is the same
    for x in range(len(banner_lines) - 1):
        if len(banner_lines[x]) > len(banner_lines[x + 1]):
            banner_lines[x + 1] += ' '
        elif len(banner_lines[x]) < len(banner_lines[x + 1]):
            banner_lines[x] += ' '
    assert all(len(banner[x]) == len(banner[x + 1])
               for x in range(len(banner_lines) - 1))
    # Now the actual splitting part
    letters = [
        tuple(line[x:x + 5] for line in banner_lines)
        for x in range(0, len(banner_lines[0]), 6)
    ]
    return letters


def read_banner(banner):
    """Reads a 5-line-high banner and returns a string."""
    banner_letters = split_banner(banner)
    return ''.join(
        LETTERS_DICT[letter]
        for letter in banner_letters
        if letter != SPACE
    )


def read_boustrophedon(multiple_line_banner):
    """Reads multiple lines of banners in alternating directions."""
    list_of_banners = split_banners(multiple_line_banner)
    text = []
    for banner in list_of_banners:
        try:
            text.append(read_banner(banner))
        except KeyError:
            text.append(read_banner(multiline_reversed(banner)))
    return ''.join(text)


def main():
    raw_i = '\n'.join(mass_input(lines=int(input()) * 6))
    print(read_boustrophedon(raw_i))


if __name__ == '__main__':
    main()
