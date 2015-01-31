import calendar

x = 1

while x < 10:
	month = int(input("Enter the month: "))
	year = int(input("Enter the year: "))
	print(calendar.month_name[month], year, "has", calendar.monthrange(year, month)[1], "days.")
	break
