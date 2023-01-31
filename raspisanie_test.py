from datetime import datetime


def return_word(number):
    if number == 0:
        return "Пн"
    elif number == 1:
        return "Вт"
    elif number == 2:
        return "Ср"
    elif number == 3:
        return "Чт"
    elif number == 4:
        return "Пт"
    elif number == 5:
        return "Сб"
    elif number == 6:
        return "Вс"


def calc_day(date_time_begin, date_time_end):
    day = date_time_begin.day()
    month = date_time_begin.month()
    year = date_time_begin.year()

    count_days = 0
    current_date_time = date_time_begin
    while current_date_time != date_time_end:
        current_day = current_date_time.day()
        count_days +=1



year = str(datetime.now())[:4]

list_of_month = [30,31,30,31,31]

date_time_begin = "01.09." + year
date_time_end = "15.01." + str(int(year) + 1)

date_time_begin = datetime.strptime(date_time_begin, "%d.%m.%Y")
print(date_time_begin)

print(return_word(date_time_begin.weekday()))

a = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб"]
