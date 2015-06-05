from utilities import input_getter
numbers = input_getter()
evens = []
for num in numbers:
	if num % 2 == 0:
		evens.append(num)

print('Count of evens: ' + str(len(evens)) + '\nEvens are:')

for even in evens:
	print(even)
