first_side = int(input("Enter side 1: "))

second_side = int(input("Enter side 2: "))

third_side = int(input("Enter side 3: "))

perimeter = first_side + second_side + third_side

print("\nEnter side 1:", first_side)

print("Enter side 2:", second_side)

print("Enter side 3:", third_side)

if first_side + second_side > third_side:
	print("Perimeter =", perimeter)
else:
	print("Invalid triangle!")
