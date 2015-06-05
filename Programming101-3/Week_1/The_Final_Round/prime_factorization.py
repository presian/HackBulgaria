def is_prime(n):
    return sum([x for x in range(1, n + 1) if n % x == 0]) == n + 1


def maximal_pow(x, n):
    result = 0
    temp_n = n
    while temp_n % x == 0:
        temp_n = temp_n // x
        result += 1
    return (x, result, n // (x ** result))


def prime_factorization(n):
    result = []
    start = 2
    while n != 1:
        if is_prime(start):
            temp = maximal_pow(start, n)
            if temp[1] != 0:
                n = n // temp[0] ** temp[1]
                result.append((temp[0], temp[1]))
                n = temp[2]
        start += 1
    return(result)


def main():
    print(prime_factorization(10))
    print(prime_factorization(14))
    print(prime_factorization(356))
    print(prime_factorization(89))
    print(prime_factorization(1000))

if __name__ == '__main__':
    main()
