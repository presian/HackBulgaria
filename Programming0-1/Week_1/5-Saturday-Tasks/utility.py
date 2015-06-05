from itertools import permutations

def checkInput():
	num = int(input("Enter a number: "))
	while num <= 1 :
		num = int(input("Enter a number: "))
	return num

def lastDigit(number):
    return number % 10, int(number // 10)

def sum_digit(n):
	digit_sum = 0
	while n is not 0:
		temp = lastDigit(n)
		current_digit = temp[0]
		rest_number = temp[1]
		digit_sum = digit_sum + current_digit
		n = rest_number
	return digit_sum

def get_triple_input():
	a = input('Enter first number: ')
	b = input('Enter second number: ')
	c = input('Enter third number: ')
	return (a, b, c)

def biggest_digit_combination(n):
	return max(set([int(''.join(digit)) for digit in permutations(n)]))

def is_even(n):
	return True if n % 2 == 0 else False

def is_prime(n):
	if n == 0 or n == 1 or (n > 2 and is_even(n)):
		return False
	elif n == 2:
		return True
	else:
		for x in range(3, int(n**0.5)+1, 2):
			if n % x == 0:
				return False
		return True
