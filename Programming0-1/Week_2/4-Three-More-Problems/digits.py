n = int(input('Enter n: '))
digits = []
while n != 0:
	digit = n % 10
	digits = [digit] + digits
	n //= 10
print('List of digits is: {}'.format(digits))

for num in digits:
	n = n * 10 + num
print('Number is: {}'.format(n))
