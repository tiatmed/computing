print("Miles Kilometers Kilometres Miles")

for i in range(1, 11):
	kilometres = 20
	print(i, round(i*1.609, 3), kilometres, round(kilometres / 1.609, 3))
	i += 1
	kilometres += 5
