"""Повернемося до нашого першого завдання з четвертого модуля і перепишемо його за допомогою функції reduce.

payment = [1, -3, 4]


def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum
Нагадаємо умову. У нас є список показань заборгованостей з комунальних послуг наприкінці місяця. 
Заборгованості можуть бути від'ємними — у нас переплата, чи додатними, якщо необхідно сплатити за рахунками. 
За допомогою reduce підсумуйте додатні значення та поверніть з функції amount_payment суму платежу в кінці місяця."""

from functools import reduce


def amount_payment(payment):
    positive_payments = reduce(lambda x,y: x + y if y > 0 else x, payment, 0 )
    return positive_payments

numbers = [100, -3, 400, 35, -100]
n = amount_payment(numbers)
print(n)