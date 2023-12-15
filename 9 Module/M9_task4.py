"""Повернемося до завдання розрахунку ціни з урахуванням дисконту та розберемо підхід із позиції карування.
Створіть функцію discount_price(discount), 
яка визначатиме в собі та повертатиме функцію розрахунку реальної ціни з урахуванням знижки.

Виклик функції discount_price(discount) поверне функцію, яка розраховує ціну на товар зі знижкою, 
що дорівнює discount .

Наприклад:

cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))
Повинен вивести:
85.0
90.0
95.0
"""

def discount_price(discount):
    # Внутрішня функція для розрахунку реальної ціни з урахуванням знижки
    def calculate_discounted_price(price):
        return price * (1 - discount)

    # Повертаємо функцію розрахунку зниженої ціни
    return calculate_discounted_price

# Приклад використання:
cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))
# Ця функція discount_price приймає параметр discount і повертає функцію calculate_discounted_price, 
# яка розраховує реальну ціну з урахуванням зазначеної знижки. 
# Потім ми створюємо три функції (cost_15, cost_10, cost_05), 
# які визначають знижку і можуть бути використані для розрахунку ціни з відповідною знижкою. 
# У прикладі це демонструється для різних рівнів знижок.
        

    