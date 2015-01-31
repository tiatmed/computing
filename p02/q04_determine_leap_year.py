x = 1

while x > 0:
	year = int(input("Enter year: "))
	if year % 4 == 0:
		print("Leap")
	elif year % 100 == 0:
		print("Non-Leap")
	elif year % 400 == 0:
		print("Leap")
	else:
		print("Non-leap")
	break
