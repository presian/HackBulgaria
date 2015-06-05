def is_prime(n):
    return sum([x for x in range(1, n + 1) if n % x == 0]) == (n + 1)


def goldbach(n):
    return [(x, n - x) for x in range(2, n // 2 + 1) if is_prime(x) and is_prime(n - x)]


def main():
    print(goldbach(4))
    print(goldbach(6))
    print(goldbach(8))
    print(goldbach(10))
    print(goldbach(100))


if __name__ == '__main__':
    main()
