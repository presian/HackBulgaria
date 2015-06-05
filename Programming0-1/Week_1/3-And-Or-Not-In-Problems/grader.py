def point_system(points):
	if 0 <= points <= 50:
		return "Слаб 2"
	elif 51 <= points <= 60:
		return "Среден 3"
	elif 61 <= points <= 70:
		return "Добър 4"
	elif 70 <= points <= 80:
		return "Много Добър 5"
	elif 81 <= points < 100:
		return "Отличен 6"
	elif points == 100:
		return "Много Отличен 7"
	else:
		return "'Нема' такава оценака!" 

print(point_system(100))