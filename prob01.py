def population(t):
    return 100 * pow(t, -2) + 201/(t+1) + 1


def main():
    i = input()
    while i != '0':
        t = int(i)
        print(t, population(t))
        i = input()

if __name__ == '__main__':
    main()
