"""Нехай є рядок з числами (з метою спрощення числа лише цілі), що визначає якісь частини загального доходу. 
Наприклад:
"The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."

Необхідно реалізувати функцію generator_numbers, 
яка буде парсити рядок і знаходити всі цілі числа в ньому та працювати як генератор, 
який буде віддавати зазначені числа при зверненні до нього у циклі.

З парсингом рядків ми вже зіштовхувалися виконуючи завдання модуля 7, 
коли розбивали на лексеми арифметичний вираз

Функція generator_numbers(string="") безпосередньо розпарсює рядок і за допомогою yield повертає поточне число.

Функція sum_profit(string) підсумовує числа, отримані від generator_numbers, 
та повертає загальну суму прибутку з рядка."""

import re

def generator_numbers(string=""):
    # Знаходимо всі цілі числа в рядку за допомогою регулярного виразу
    numbers = re.findall(r'\b\d+\b', string)

    # Перебираємо знайдені числа та повертаємо їх як генератор
    for number in numbers:
        yield int(number)

def sum_profit(string):
    # Викликаємо generator_numbers та підсумовуємо отримані числа
    total_profit = sum(generator_numbers(string))
    return total_profit

# Приклад використання:
profit_string = "The resulting profit was: from the southern possessions $100, from the northern colonies $500, and the king gave $1000."
total_profit = sum_profit(profit_string)

print("Total Profit:", total_profit)