score = int(input("Enter a score between 0 and 100 inclusive: "))

if 0 <= score <= 100:
	if 70 <= score <= 100:
		print("A")
	if 60 <= score <= 69:
		print("B")
	if 55 <= score <= 59:
		print("C")
	if 50 <= score <= 54:
		print("D")
	if 45 <= score <= 49:
		print("E")
	if 35 <= score <= 44:
		print("S")
	if 0 <= score <= 35:
		print("U")
else:
	print("Invalid! Score must be within 0 - 100.")
