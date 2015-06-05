
n = input('Enter n ')
digits = []
for ch in n:
    digits.append(int(ch))

big = ''
for d in sorted(digits):
    big += str(d)
big_num = int(big)
small = ''
for d in sorted(digits, reverse=True):
    small += str(d)
small_num = int(small)

print('Largest: {}'.format(big_num))
print('Smallest: {}'.format(small_num))
