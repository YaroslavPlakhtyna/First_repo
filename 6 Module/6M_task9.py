"""Є два рядки у різних кодуваннях - "utf-8" та "utf-16".
Нам необхідно зрозуміти, чи дорівнюються рядки між собою.

Реалізуйте функцію is_equal_string(utf8_string, utf16_string),
яка повертає True, якщо рядки дорівнюють собі, і False — якщо ні."""

def is_equal_string(utf8_string, utf16_string):
    try:
        utf8_string_converted = utf8_string.decode('utf-8')
        utf16_string_converted = utf16_string.decode('utf-16')
        return utf8_string_converted == utf16_string_converted
    except UnicodeError:
        # Якщо виникає помилка при конвертації, то рядки не дорівнюються
        return False
