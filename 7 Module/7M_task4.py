"""Далі підуть завдання на повторення та закріплення матеріалу. Можна використовувати будь-які техніки,
з якими ви зіткнулися у процесі навчання. І почнемо ми з функцій.

У Python існує рядкова функція isdigit(). Ця функція повертає True, якщо всі символи в рядку є цифрами,
і є принаймні один символ, інакше — False. Напишіть функцію з ім'ям is_integer,
яка розширюватиме функціональність isdigit(). При перевірці рядка необхідно ігнорувати початкові
та кінцеві прогалини в рядку. Після виключення зайвих прогалин рядок вважається таким,
що представляє ціле число, якщо:

- її довжина більша або дорівнює одному символу
- вона повністю складається з цифр
- передбачити виняток, що, можливо, є початковий знак "+" або "-", після якого мають йти цифри"""

def is_integer(s):
    # Remove leading and trailing whitespaces
    s = s.strip()

    if len(s) == 0:
        return False

    # Check for a valid integer
    try:
        int(s)
        return True
    except ValueError:
        # The string couldn't be converted to an integer
        return False
    
# Test cases
print(is_integer("123"))      # True
print(is_integer("   456"))   # True
print(is_integer("-789"))      # True
print(is_integer("+42"))       # True
print(is_integer("  12a3  "))  # False (contains non-digit character)
print(is_integer(""))          # False (empty string)