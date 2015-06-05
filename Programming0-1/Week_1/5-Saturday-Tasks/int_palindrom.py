n = input('Please enter a number: ')
if int(n) == int(n[::-1]):
	print('The number is palindrom!')
else:
	print('The number is not palindrom!')
