#reads a Fahrenheit degree in double (floating point / decimal) from standard input, then converts it to Celsius and displays the result in standard output

fahrenheit = input("Enter the temperature in Fahrenheit degree in double: ")

celsius = (5/9) * (float(fahrenheit) - 32)

print(celsius)

