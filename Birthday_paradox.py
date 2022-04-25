from datetime import date
from random import randint


# today = date.today()
# print(today)

# my_birthday = date(2001, 10, 3)
# print(my_birthday)
# print(my_birthday.fromordinal(my_birthday.toordinal()))
# print(my_birthday.toordinal())
# print(my_birthday.ctime())
# my_set = my_birthday.ctime().split()
# print(my_set)

start = date(2022, 1, 1).toordinal()
end = date(2022, 12, 31).toordinal()

random_date = date.fromordinal(randint(start, end))
random_date = random_date.ctime()
days = [date.fromordinal(randint(start, end)).ctime().split() for _ in range(23)]
print(days)
birthdays = list(map(lambda x: tuple(x[1:3]), days))
print(birthdays)
birthdays = set(birthdays)
print(birthdays)
if len(days) > len(birthdays):
    print('Дни рождения совпали! Хотя бы два дня рождения пришлись на одну и ту же дату')
