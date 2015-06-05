num = int(input('Please enter a number: '))


if num % 2 == 0:
	result = ' is even'
else:
	result = ' is odd'

print(str(num) + result)
