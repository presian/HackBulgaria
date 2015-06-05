a = int(input('Please enter first number: '))
b = int(input('Please enter second number: '))

format_big = '{0}({1}) is bigger than {2}({3})'
format_equal = '{0}({1}) is equal to {2}({3})'

if a > b:
	print(format_big.format('a', str(a), 'b', str(b)))
elif b > a:
	print(format_big.format('b', str(b), 'a', str(a)))
else:
	print(format_equal.format('a', str(a), 'b', str(b)))
