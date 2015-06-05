def inner_trim(string):
	first_step = string.strip()
	second_step = ''
	for ch in first_step:
		if ch == ' ':
			if second_step[-1:] != ' ':
				second_step += ch
		else:
			second_step += ch
	print(second_step)
def main():
	inner_trim("Python    Django")
	inner_trim("  Python     Django   ")

if __name__ == '__main__':
	main()