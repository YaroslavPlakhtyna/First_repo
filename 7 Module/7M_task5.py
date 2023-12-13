"""Дуже часто люди у своїх повідомленнях не ставлять великі літери,
особливо це стало масовим явищем в еру мобільних. пристроїв.
Розробіть функцію capital_text, яка прийматиме на вхід рядок з текстом і повертатиме рядок
з відновленими великими літерами.

Функція повинна:

зробити великою першу літеру в рядку, попри прогалини
зробити великою першу літеру після точки, попри прогалини
зробити великою першу літеру після знака оклику, попри прогалини
зробити великою першу літеру після знака питання, попри прогалини"""

def capital_text(s):
    result= ""
    capitaize_next=True # Flag to track when to capitalize the next character
    for char in s:
        if capitaize_next and char.isalpha():
            result += char.upper()
            capitaize_next = False
        else:
            result += char.lower()
        
        if char in ['.','!', '?']:
            capitaize_next = True
    return result