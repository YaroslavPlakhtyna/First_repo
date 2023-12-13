"""Повернемося до попереднього завдання та виконаємо зворотне.
Напишіть рекурсивну функцію encode для кодування списку або рядка.
Як аргумент функція приймає список ( наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ])
або рядок (наприклад, "XXXZZXXYYYZZ").
Функція повинна повернути закодований список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2])."""

def encode(data):
    if len(data) == 0 or not data:
        return []
    
    counts = 1
    char = data[0]
    
    for el in data:
        if not char == el:
            counts -= 1
            if len(data[counts:]) > 0:
                return [char] + [counts] + encode(data[counts:])
            else:
                return [char] + [counts]
        
        if counts == len(data):
            return [char] + [counts]

        counts += 1