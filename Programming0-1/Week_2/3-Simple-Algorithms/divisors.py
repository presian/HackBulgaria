def getDivisorsList():
	n = int(input('Enter n: '))
	divisors = []
	for num in range(1, n):
		if n % num == 0:
			divisors.append(num)
	return divisors

if __name__ == '__main__':
	print(getDivisorsList())
