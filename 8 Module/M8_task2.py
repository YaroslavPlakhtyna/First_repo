"""Напишіть функцію визначення кількості днів у конкретному місяці. 
Ваша функція повинна приймати два параметри: month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12
 і year - рік, що складається із чотирьох цифр.
Перевірте, чи функція коректно обробляє місяць лютий високосного року."""

from datetime import date

def get_days_in_month(month, year):
    # Перевірка на коректність вхідних даних
    if not (1 <= month <= 12) or not (1000 <= year <= 9999):
        raise ValueError("Неправильні значення для місяця або року")

    # Місяці, які мають 31 день
    thirty_one_days = {1, 3, 5, 7, 8, 10, 12}

    # Місяці, які мають 30 днів
    thirty_days = {4, 6, 9, 11}

    # Якщо це лютий
    if month == 2:
        # Перевірка на високосний рік
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28

    # Якщо місяць має 31 день
    elif month in thirty_one_days:
        return 31
    # Якщо місяць має 30 днів
    elif month in thirty_days:
        return 30
    else:
        raise ValueError("Невідомий місяць")
        
print(days_in_month(2, 2020))  # Високосний рік, лютий має 29 днів
print(days_in_month(2, 2021))  # Невисокосний рік, лютий має 28 днів
print(days_in_month(4, 2021))  # Квітень має 30 днів
print(days_in_month(12, 2022)) # Грудень має 31 день