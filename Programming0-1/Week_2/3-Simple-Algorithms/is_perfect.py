from Utilities import is_mersenne_prime


def is_number_perfect(number):
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

if __name__ == '__main__':
    n = int(input('Enter n: '))
    if is_number_perfect(n) is True:
        print('{} is perfect number!'.format(n))
    else:
        print('{} is not perfect number!'.format(n))
