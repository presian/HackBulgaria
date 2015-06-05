def input_getter():
	n = int(input('Enter n: '))
	numbers = []
	for x in range(0, n):
		numbers.append(int(input('Enter a number: ')))
	return numbers

def string_input_getter():
	n = int(input('Enter n: '))
	words = []
	for x in range(0, n):
		words.append(input('Enter a word: '))
	return words
