"""numbers = [0, 1, 2, 3]
new = numbers[::-1] # Отримати список `numbers` у зворотному порядку
print(new) # [3, 2, 1, 0]"""

"""Ми розробляємо кулінарний блог. І в рецептах, при написанні списку інгредієнтів,
ми розділяємо їх комами, а перед останнім ставимо союз "and", як у прикладі нижче:
2 eggs, 1 liter sugar, 1 tsp salt and vinegar
Напишіть функцію format_ingredients, яка прийматиме на вхід список
з інгредієнтів ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] та повертатиме рядок зібраний
з його елементів в описаний вище спосіб.
Ваша функція має вміти обробляти списки будь-якої довжини."""

def format_ingredients (items):
    if not items:
        return ""
    elif len(items) == 1:
        return items[0]
    else:
        items1 = items[:-1]
        items2 = items[-1]
        result = ", ".join(items1) + " and " + items2
        return result

"""def format_ingredients (items):
    if not items:
        return "" 
    if len(items) == 1:
        return items[0]
    formatted_string = ", ".join(items[:-1]) + " and " + items[-1]
    return formatted_string"""

ingredients_list = []
formatted_ingredients = format_ingredients(ingredients_list)
print(formatted_ingredients)