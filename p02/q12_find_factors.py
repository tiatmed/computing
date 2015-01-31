"""
Write a program that reads an integer and displays all its smallest factors. 
For example, if the input integer is 120, the output should be as follows: 2, 2, 2, 3, 5.
"""
    
number = int(input("Enter an integer: "))
factors = []

for i in range(1, int(number ** 0.5 + 1)):
	if number % i == 0:
		factors.append(i)
		factors.append(int(number / i))
		
print(factors)

