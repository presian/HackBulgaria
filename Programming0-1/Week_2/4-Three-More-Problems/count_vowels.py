sentence = input('Enter a sentence: ')

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

counter = 0
for ch in sentence:
	for c in vowels:
		if ch.lower() == c:
			counter += 1

print('"{}" - {}'.format(sentence, counter))