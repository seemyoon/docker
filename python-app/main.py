import calendar

print('Welcome to the calendar\n')

year = int(input('Enter the year: '))
month = int(input('Enter any month number: '))
print(calendar.month(year, month))
