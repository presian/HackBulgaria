from utilities import string_input_getter

words = string_input_getter()
print('Sorted names are:')
for word in sorted(words):
	print(word)
