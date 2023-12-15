"""Реалізуйте функцію get_discount_price_customer для розрахунку ціни на товар інтернет-магазину 
з урахуванням знижки клієнта.

Функція приймає два параметри:

price — ціна продукту
customer — словник з даними клієнта такого виду: {"name": "Dima"} або {"name": "Boris", "discount": 0.15}
Ви маєте глобальну змінну DEFAULT_DISCOUNT, яка визначає знижку для клієнта, якщо у нього немає поля discount.

Функція get_discount_price_customer має повертати нову ціну товару для клієнта.

Нагадаємо, що дисконт discount - це дробове число від 0 до 1.
І ми під знижкою розуміємо коефіцієнт, який визначає величину ціни. 
І на цю величину ми знижуємо підсумкову ціну товару: price = price * (1 - discount)."""

DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    # Отримуємо знижку клієнта або встановлюємо дефолтну
    customer_discount = customer.get("discount", DEFAULT_DISCOUNT)

    # Розрахунок нової ціни з урахуванням знижки
    discounted_price = price * (1 - customer_discount)

    return discounted_price
    
# Приклад використання:
product_price = 100
customer1 = {"name": "Dima"}
customer2 = {"name": "Boris", "discount": 0.15}

price_for_customer1 = get_discount_price_customer(product_price, customer1)
price_for_customer2 = get_discount_price_customer(product_price, customer2)

print(f"Ціна для клієнта 1: {price_for_customer1}")
print(f"Ціна для клієнта 2: {price_for_customer2}")
    
        