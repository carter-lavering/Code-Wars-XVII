def population(t):
    return 100 * (t ** 0.5) + 201/(t+1) + 1

def main():
    i = input()
    while i != '0':
        t = int(i)
        print(t, round(population(t)))
        i = input()

if __name__ == '__main__':
    main()
