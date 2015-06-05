a = int(input('Please enter down boundary: '))
b = int(input('Please enter upper boundary: '))
x = int(input('Please enter your number: '))

if a < x < b:
	print("The number is in the interval")
elif x == a:
	print("The number is equal to the lower bound of the interval")
elif x == b:
	print("The number is equal to the upper bound of the interval")
elif x < a:
	print("The number is outside the interval, x < a")
else:
	print("The number is outside the interval, x > b")
