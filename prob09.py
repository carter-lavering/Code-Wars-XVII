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


def prime_generator(cap):
    number = 3
    primes = [2]
    yield 2
    while number <= cap:
        number_is_prime = all(number % prime != 0 for prime in primes)
        if number_is_prime:
            primes.append(number)
            yield number
        number += 1


def is_prime(n):
    primes = list(prime_generator(n))
    return n in primes


def goldbach_conjecture(n):
    """Returns a list of pairs of primes that add up to n."""
    half_of_n = n // 2
    while not (is_prime(half_of_n) and is_prime(n - half_of_n)):
        half_of_n -= 1
    assert is_prime(half_of_n)
    assert is_prime(n - half_of_n)
    return (half_of_n, n - half_of_n)


def main():
    all_input = mass_input(end='0')
    for i in all_input:
        i = int(i)
        a, b = goldbach_conjecture(i)
        print(a, '+', b, '=', i)


if __name__ == '__main__':
    main()
