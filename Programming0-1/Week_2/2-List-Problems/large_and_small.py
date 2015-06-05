n = input('Enter n: ')
digits = []
for char in n:
	digits.append(int(char))

small_list = ''
for d in sorted(digits):
	small_list += str(d)

bigg_list = ''
for digit in sorted(digits, reverse=True):
	bigg_list += str(digit)
small_number = int(''.join(small_list))
bigg_number = int(''.join(bigg_list))
print('Smallest: {0}'.format(small_number))
print('Largest: {0}'.format(bigg_number))
