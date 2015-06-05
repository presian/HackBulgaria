from utilities import string_input_getter
word = input('Enter a word for research: ')
words = string_input_getter()

counter = 0
for w in words:
	if w == word:
		counter += 1

print('{0} is found {1} times.'.format(word, counter))
