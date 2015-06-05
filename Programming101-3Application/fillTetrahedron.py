import math

def fill_tetrahedron(num):
	volume_tetrahedron = (math.sqrt(2)*math.pow(num,3))/12
	water_in_tetrahedron = volume_tetrahedron / 1000 # 1l = 1000 cm3
	return round(water_in_tetrahedron, 2)

# For easy testing!
# a = int(input('Enter number: '))
# print(fill_tetrahedron(a))
