"""
Створіть функцію decimal_average(number_list, signs_count), 
яка обчислюватиме середнє арифметичне типу Decimal з кількістю значущих цифр signs_count. 
Параметр number_list — список чисел

--- Увага !!! ---
Не забувайте приводити всі числа у списку до типу `decimal`

Приклад:
виклик функції decimal_average([3, 5, 77, 23, 0.57], 6) поверне 21.714
виклик функції decimal_average([31, 55, 177, 2300, 1.57], 9) поверне 512.91400
"""

from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    number_sum = 0
    for i in number_list:
        number_sum += Decimal(i)
    getcontext().prec = signs_count
    average = number_sum / Decimal(len(number_list))
    return average

signs_count = 6
number_list = [3, 5, 77, 23, 0.57]
res = decimal_average(number_list, signs_count)
print(res)
    