LETTERS = """..A..
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


def split_letters(string):
    letters_dict = {
        letter: [line for line in string.split('\n') if letter in line]
        for letter in ALPHABET
    }
    return letters_dict

def read_banner(banner):
    banner = banner.split('\n')



def main():
    raw_i = mass_input(lines=int(input()) * 6)
    output_string = ''
    for b_line in split_banner(raw_i):  # banner_line
        try:
            s_line = read_banner(b_line)
        except LookupError:
            s_line = read_banner(backwards(b_line))
        output_string += s_line
    print(output_string)


if __name__ == '__main__':
    main()
