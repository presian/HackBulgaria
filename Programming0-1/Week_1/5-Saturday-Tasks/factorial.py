n = int(input('Please enter a number: '))

factor = 1

if n == 0:
	print(factor)
else:
	for index in range(1, n+1):
		factor = factor * index
	print(factor)
