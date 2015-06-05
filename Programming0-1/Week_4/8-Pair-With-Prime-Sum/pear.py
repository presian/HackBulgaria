from math import sqrt


def is_prime(n):
    if n == 2:
        return True
    elif (n % 2 == 0 and n > 2) or n == 1:
        return False
    else:
        for num in range(3, int(sqrt(n)) + 1, 2):
            if n % num == 0:
                return False
        return True


def prime_pair(numbers):
    length = len(numbers)
    for i in range(0, length):
        for j in range(i, length):
            if is_prime(numbers[i] + numbers[j]):
                return True
    return False

print(prime_pair([1, 2, 3, 4, 5]))
