"""Всім відомо, що для доступу до кредитної картки банку потрібний пін-код.
Класично склалося, що це поєднання чотири цифри.
Нам необхідно вирішити наступне програмістське завдання.
Є підготовлений перелік пін-кодів. Напишіть функцію is_valid_pin_codes,
яка буде приймати як параметр список цих пін-кодів — рядок з чотирьох цифр 
і повертати логічне значення — валідний список чи ні.
Переконайтеся, що серед цих пін-кодів у списку не буде дублікатів,
всі вони зберігаються у вигляді рядків, їх довжина дорівнює 4 символам і містять вони тільки цифри.

Приклад аргументу для функції is_valid_pin_codes:
['1101', '9034', '0011']

Якщо список відповідає всім поставленим умовам, функція повертає логічне значення True.
Якщо хоч одну з умов порушено, повертається значення — False.
Передбачити перевірку на порожній список в аргументі функції та повернути при цьому значення False."""

#def is_valid_pin_codes(pin_codes):
#    for numbers in pin_codes:
#        for i in range(0, len(numbers), 4):
#            group_of_4 = numbers[i:i:+4]
#        if group_of_4 == set(pin_codes):
#            return True 
#        else:
#            return False
#
#print(is_valid_pin_codes(['1101', '9034', '0011']))

def is_valid_pin_codes(pin_codes):
    if not pin_codes:
        return False
    if len(pin_codes) != len(set(pin_codes)):
        return False
    for code in pin_codes:
        if not (isinstance(code, str) and len(code) == 4 and code.isdigit()):
            return False
    return True

pin_codes_example = ['1101', '9034', '0011']
result = is_valid_pin_codes(pin_codes_example)
print(result)

# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
#   isinstance(object, type)
#
# The isdigit() method returns True if all the characters are digits, otherwise False.
# Exponents, like ², are also considered to be a digit.
#   string.isdigit()
