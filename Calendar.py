from datetime import date, timedelta  # import modul of date and function of timedelta

# constants
days = ('SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT')
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')

while True:
    year = input('Put in an year that you want to check')
    if not year.isdigit():
        print('Please put in a number of the year')
        continue
    elif year.isdigit():
        break

while True:
    month = int(input('Put in a number of the month, from 1 to 12'))
    if month not in range(1, 13):
        print('Please write a number, like 10 for October')
        continue
    else:
        break


def generate_calendar(month, year):
    hat = ''  # here it will be a calendar in text type
    hat += (' ' * 25) + months[month - 1] + ' ' + year + '\n'
    hat += '...SUN.....MON.....TUE.....WED.....THU.....FRI.....SAT...\n'
    week_separator = ('+-------' * 7) + '+\n'  # string-separator
    empty_row = ('|       ' * 7) + '|\n'

    current_date = date(int(year), month, 1)  # first number of our date
    while current_date.weekday() != 6:  # because Sunday in weekday code is 6
        current_date -= timedelta(days=1)
    while True:  # pass by the loop along all weeks in the month
        hat += week_separator

        day_number_row = ''  # the row with marks of the days numbers
        for i in range(7):
            day_number_mark = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_mark + (' ' * 5)
            current_date += timedelta(days=1)
        day_number_row += '|\n'
        hat += day_number_row
        for i in range(3):
            hat += empty_row

        if current_date.month != month:
            break

    hat += week_separator
    return hat


cal_text = generate_calendar(month, year)
print(cal_text)

calendar_file_name = f'Calendar_on_Python_by_me_{year}_{month}.txt'
with open(calendar_file_name, 'w') as file:
    file.write(cal_text)

print('Saved to ' + calendar_file_name)









