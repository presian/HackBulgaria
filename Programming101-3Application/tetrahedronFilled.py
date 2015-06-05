from fillTetrahedron import fill_tetrahedron

def tetrahedron_filled(tetrahedrons, water):
	tetrahedrons_water_volumes = []
	for t in tetrahedrons:
		tetrahedrons_water_volumes.append(fill_tetrahedron(t))
	tetrahedrons_water_volumes.sort()
	counter = 0
	for vol in tetrahedrons_water_volumes:
		water -= vol
		if water >= 0:
			counter += 1 
		else:
			break
	return counter

# For easy testing!
print(tetrahedron_filled([100, 20, 30], 10))
