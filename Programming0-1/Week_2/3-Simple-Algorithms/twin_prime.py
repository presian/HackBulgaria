from Utilities import isPrime

n = int(input('Enter p: '))
output = ''
if isPrime(n) == False:
	output = '{0} is not a prime.'.format(n)
else:
	output = 'Twin primes with {0}:'.format(n)	
	if isPrime(n - 2):
		output += '\n{0},{1}'.format(n - 2, n)
	if isPrime(n + 2):
		output += '\n{0},{1}'.format(n, n + 2)
	if (not isPrime(n - 2)) and (not isPrime(n + 2)):
		output += '\n{0} is not\n{1} is not'.format(n - 2, n + 2)
print(output)
