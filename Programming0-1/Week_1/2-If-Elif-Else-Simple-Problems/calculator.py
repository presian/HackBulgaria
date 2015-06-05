a = int(input('Please enter first number: '))
b = int(input('Please enter second number: '))
operator = input('Please enter operator: ')


if operator == '+':
	result = 'Result is: ' + str(a + b)
elif operator == '-':
	result = 'Result is: ' + str(a - b)
elif operator == '*':
	result = 'Result is: ' + str(a * b)
elif operator == '/':
	result = 'Result is: ' + str(a / b)
else:
	result = 'We do not support that operation.'

print(result)
