"""
Enter name: Lim Ah Seng
Enter number of hours worked weekly: 10
Enter hourly pay rate: 6.75
Enter CPF contribution rate(%): 20

Sample output:

Payroll statement for Lim Ah Seng
Number of hours worked in week: 10
Hourly pay rate: $6.75
Gross pay = $67.50
CPF contribution at 20% = $13.50
Net pay = $54.00

"""

name = input("Enter name: ")

hours_worked = int(input("Enter number of hours worked weekly: "))

pay_rate = float(input("Enter hourly pay rate: ")) 

cpfrate = int(input("Enter CPF contribution rate(%): "))

gross_pay = hours_worked * pay_rate

cpf = cpfrate / 100 * gross_pay

netpay = gross_pay - cpf

print("Payroll statement for", name)

print("Number of hours worked in week: ", hours_worked)

print("Hourly pay rate = $", pay_rate)

print("Gross pay = $", gross_pay)

print("CPF contribution at", cpfrate, "% = $", cpf)

print("Net pay = $", netpay)
