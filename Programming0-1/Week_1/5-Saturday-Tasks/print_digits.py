from utility import lastDigit 

n = int(input('Please enter number: '))

while n is not 0:
	temp = lastDigit(n)
	print(temp[0])
	n = temp[1]
