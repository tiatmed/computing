"""
A solution to find the greatest common divisor of two integers n1 and n2 is as follows: 
First find d to be the minimum of n1 and n2, then check whether d, d-1, … d-2, 2, or 1 is a divisor for both 
n1 and n2 in this order. The first such common divisor is the greatest common divisor for n1 and n2. 
Write a program to implement this solution.
"""

n1 = int(input("Enter integer 1: "))
n2 = int(input("Enter integer 2: "))

d = min(n1, n2)

while d > 0:
	if n1 % d == 0:
		if n2 % d == 0:
			print(d, "is the greatest common divisor for", n1, "and", n2)
			break
	d -= 1
