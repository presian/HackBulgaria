def caesar_encrypt(input_str, n):
	output = ''
	for char in input_str:
		if char.isdigit():
			output + char
		else:
			if char.istitle() and (ord(char) + n) > 90: # 90 is code of 'Z'
				n = n - (90 - ord(char))
				output += chr(65 + n - 1) # 65 is code of 'A'
			elif (ord(char) + n) > 122: # 122 is code of 'z'
				n = n - (122 - ord(char))
				output += chr(97 + n - 1) # 97 code of 'a'
			else:
				output += chr(ord(char) + n)
	return output

# Little testing ;)
# print(caesar_encrypt("abc", 1))
# print(caesar_encrypt("ABC", 1))
# print(caesar_encrypt("abc", 2))
# print(caesar_encrypt("aaa", 7))
# print(caesar_encrypt("xwz", 1))
# print(caesar_encrypt("XWZ", 1))
# print(caesar_encrypt("XWZ", 2))
