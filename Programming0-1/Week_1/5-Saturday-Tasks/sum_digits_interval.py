from utility import sum_digit

n = int(input('Enter N: '))
m = int(input('Enter M: '))

min_num = min(n, m)
max_num = max(n, m)
while min_num <= max_num:
	print('Sum of digits of {0} = {1}'.format(min_num, sum_digit(min_num)))
	min_num += 1
