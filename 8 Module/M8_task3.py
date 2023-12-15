"""Напишіть функцію get_str_date(date), 
яка перетворюватиме дату з бази даних у форматі ISO '2021-05-27 17:08:34.149Z' 
у вигляді наступного рядка 'Thursday 27 May 2021' - день тижня, число, місяць та рік. 
Перетворене значення функція повертає під час виклику."""

from datetime import datetime


def get_str_date(date):
    # Перетворення рядка у форматі ISO в об'єкт datetime
    date_object = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')

    # Форматування дати у бажаний вигляд
    formatted_date = date_object.strftime('%A %d %B %Y')

    return formatted_date

# Приклад виклику функції
date_from_db = '2021-05-27 17:08:34.149Z'
result = get_str_date(date_from_db)
print(result)