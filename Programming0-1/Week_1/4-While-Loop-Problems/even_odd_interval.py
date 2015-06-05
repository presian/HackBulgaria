a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for x in range(min(a, b), max(a, b) + 1):
	print("{0} - {1}".format(x, 'even' if (x % 2 == 0) else 'odd'))
