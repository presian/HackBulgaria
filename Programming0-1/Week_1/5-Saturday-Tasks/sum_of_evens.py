from utility import checkInput, is_even

n = checkInput()
decreaser = 0 if is_even(n) else 1
n = n - decreaser
sum = 0
while n >= 1:
	sum += n
	n -= 2
print(sum)
