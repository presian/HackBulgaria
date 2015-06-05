from Utilities import is_mersenne_prime

n = int(input('Enter n: '))
index = 2
while True:
    if n == 0:
        break
    if is_mersenne_prime(index):
        euler_thing = (2 ** (index - 1)) * ((2 ** index) - 1)
        print(euler_thing)
        if index == 2:
            index += 1
        else:
            index += 2
        n -= 1
    else:
    	index += 2
