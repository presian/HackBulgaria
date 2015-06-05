from math import sqrt

def isPrime(n):
    if n == 2:
        return True
    elif (n % 2 == 0 and n > 2) or n == 1:
        return False
    else:
        for num in range(3, int(sqrt(n)) + 1, 2):
            if n % num == 0:
                return False
        return True


def is_mersenne_prime(n):
    meserenne_power = (2 ** n) - 1
    if isPrime(meserenne_power) is True:
        return True
    return False
