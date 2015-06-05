n = input('Please enter first integer: ')
m = input('Please enter second integer: ')

print(n[-1:] 
	if (int(n[-1:]) > int(m[-1:])) 
	else m[-1:] 
	if (int(n[-1:]) < int(m[-1:]))
	else n
	if (int(n) > int(m))
	else m)
