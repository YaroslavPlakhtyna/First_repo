"""Як ми знаємо, ключ у словнику має бути унікальним, тоді як значення його ні.
Реалізуйте функцію lookup_key для пошуку всіх ключів за значенням у словнику.
Першим параметром у функцію ми передаємо словник, а другим — значення, що хочемо знайти.
Таким чином, результат може бути як список ключів, так і порожній список, якщо ми нічого не знайдемо."""


def lookup_key(data, value):
    keys_list = [key for key, val in data.items() if val == value] 
    return keys_list

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1}
search_value = 1
result = lookup_key(my_dict, search_value)

print(f"Keys for value {search_value}: {result}")



# keys_list = [key for key, val in dictionary.items() if val == value]
# 
# This line uses a list comprehension to create a list (keys_list) by iterating over the items
# of the dictionary and selecting keys where the corresponding values match the specified value.
# 
# Here's a detailed explanation:
# 1. List Comprehension Structure:
# 
# keys_list = [expression for item in iterable if condition]
# 
# In this case:
# 'expression' is 'key' (the value to include in the list),
# 'item' is a tuple '(key, val)' obtained from iterating over 'dictionary.items()',
# 'iterable' is 'dictionary.items()', which provides key-value pairs,
# 'condition' is 'if val == value'.
# 
# 2. Iteration Over dictionary.items():
# 
# for key, val in dictionary.items()
# 
# Here, we iterate over each key-value pair in the dictionary using 'dictionary.items()'. 
# In each iteration, 'key' takes the key, and 'val' takes the corresponding value.
# 
# 3. Condition:
# 
# if val == value
# 
# This condition checks whether the value ('val') in the current key-value pair is equal
# to the specified value ('value'). If the condition is 'True', the key is included in the list;
# otherwise, it is excluded.
# 
# 4. Resulting List:
# 
# keys_list = [key for key, val in dictionary.items() if val == value]
# The list comprehension generates a new list ('keys_list') containing only the keys where
# the corresponding values match the specified value.
# 
# Here's a step-by-step example:
# 
# dictionary = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1}
# value = 1
# 
# keys_list = [key for key, val in dictionary.items() if val == value]
# print(keys_list)
# 
# The output will be: ['a', 'c', 'e']
# This means that the keys 'a', 'c', and 'e' have values equal to '1' in the dictionary.