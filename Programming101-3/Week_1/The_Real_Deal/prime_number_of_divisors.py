from is_prime import is_prime


def prime_number_of_divisors(n):
    return is_prime(sum([1 for x in range(1, n + 1) if n % x == 0]))


def main():
    print(prime_number_of_divisors(7))
    print(prime_number_of_divisors(8))
    print(prime_number_of_divisors(9))


if __name__ == '__main__':
    main()
