from math import sqrt


def getDivisorsList():
    n = int(input('Enter n: '))
    divisors = []
    for num in range(1, n):
        if n % num == 0:
            divisors.append(num)
    return divisors
# print(getDivisorsList())


def sum_ints():
    return sum(getDivisorsList())
# print(sum_ints())


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
# print(is_prime(12))


def is_mersenne_prime(n):
    meserenne_power = (2 ** n) - 1
    if is_prime(meserenne_power) is True:
        return True
    return False


def is_perfect(number):
    if number < 6 or number % 2 == 1:
        return False
    elif number == 6:
        return True
    index = 3
    while True:
        if is_mersenne_prime(index) is True:
            euler_thing = (2 ** (index - 1)) * ((2 ** index) - 1)
            if euler_thing > number:
                return False
            elif euler_thing == number:
                return True
        index += 2
# print(is_perfect(8589869056))


def first_n_perfects(n):
    perfects = []
    index = 2
    while True:
        if n == 0:
            break
        if is_mersenne_prime(index):
            euler_thing = (2 ** (index - 1)) * ((2 ** index) - 1)
            perfects.append(euler_thing)
            if index == 2:
                index += 1
            else:
                index += 2
            n -= 1
        else:
            index += 2
    return perfects
# print(first_n_perfects(6))


def is_any_prime(n):
    while n > 0:
        num = n % 10
        n //= 10
        if is_prime(num) is True:
            return True
    return False
# print('Yes' if is_any_prime(123) else 'No')


def tween_prime(n):
    output = ''
    if is_prime(n) == False:
        output = '{0} is not a prime.'.format(n)
    else:
        output = 'Twin primes with {0}:'.format(n)
        if is_prime(n - 2):
            output += '\n{0},{1}'.format(n - 2, n)
        if is_prime(n + 2):
            output += '\n{0},{1}'.format(n, n + 2)
        if (not is_prime(n - 2)) and (not is_prime(n + 2)):
            output += '\n{0} is not\n{1} is not'.format(n - 2, n + 2)
    return output
# print(tween_prime(23))
