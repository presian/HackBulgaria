from Utilities import isPrime

n = int(input('Enter n: '))

def have_one_prime_digit(n):
    while n > 0:
        num = n % 10
        n //= 10
        if isPrime(num) is True:
            return True
    return False

print('Yes' if have_one_prime_digit(n) else 'No')	