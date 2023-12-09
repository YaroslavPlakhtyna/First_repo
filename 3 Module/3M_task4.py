"""
Необхідно реалізувати функцію розрахунку ціни товару зі знижкою discount_price. 
Функція приймає ціну price та знижку discount — це дрібне число від 0 до 1. 
Тут і надалі ми під знижкою розумітимемо коефіцієнт, який визначає розмір від ціни.
І на цей розмір ми знижуємо підсумкову вартість товару. 
Логіку функції необхідно прописати у внутрішній функції apply_discount,
використовуючи оголошення зміною price як nonlocal.
"""

def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price1 = price * discount
        price -= price1
        
    apply_discount()
    return price
