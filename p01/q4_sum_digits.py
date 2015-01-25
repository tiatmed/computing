number = int(input("Enter an integer between 0 and 1000 here: "))

third_digit = number % 10

second_digit = number // 10 % 10

first_digit = number // 10 // 10 % 10

print(third_digit + second_digit + first_digit)
