import calendar

print('Welcome to the dockercalendar\n')

year = int(input('Please enter the year: '))
month = int(input('Enter any month number: '))

print(calendar.month(year, month))

print('Goof luck!')