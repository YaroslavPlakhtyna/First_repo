"""Напишіть функцію real_len, яка підраховує
та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'
"""
def real_len(text):
    ignored_chars = ["\n","\f","\r","\t","\v"]
    cleaned_string = "".join(char for char in text if char not in ignored_chars)
    return len(cleaned_string)

input_str1 = 'Alex\nKdfe23\t\f\v.\r'
input_str2 = 'Al\nKdfe23\t\v.\r'

result1 = real_len(input_str1)
result2 = real_len(input_str2)

print(result1) 
print(result2) 