from utility import is_prime

n = abs(int(input('Enter a number: ')))
print('The number is prime!' if is_prime(n) else 'The number is not prime!')
