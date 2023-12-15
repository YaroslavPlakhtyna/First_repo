"""Є список IP адрес:

IP = [
    "85.157.172.253",
    ...
]
Реалізуйте дві функції. Перша get_count_visits_from_ip за допомогою Counter повертатиме словник, де ключ це IP,
а значення – кількість входжень у вказаний список.

Приклад:
{
    '85.157.172.253': 2,
    ...
}
Друга функція get_frequent_visit_from_ip повертає кортеж з найбільш часто уживаним в списку IP 
і кількістю його появ в списку.

Приклад:
('66.50.38.43', 4)
"""

from collections import Counter


def get_count_visits_from_ip(ips):
    collections = Counter(ips)
    return collections
    
def get_frequent_visit_from_ip(ips):
    collections = Counter(ips)
    return collections.most_common(1)[0] #В цьому випадку, повертає перший елемент списку, що є кортежем, і функція повертає сам цей кортеж.
#У вашій функції get_frequent_visit_from_ip, ви вже повертаєте результат у вигляді tuple,
# оскільки collections.most_common(1) повертає список кортежів (наприклад, [(ip, frequency)]). 
# Проте, якщо ви хочете, щоб функція завжди повертала сам кортеж (а не список, який містить один кортеж), 
# ви можете застосувати індексацію, щоб отримати перший (і єдиний) елемент списку.

IP = [
    "85.157.172.253",
    "86.157.172.253",
    "85.157.172.253",
    "87.157.172.253",
    "88.157.172.253",
    "88.157.172.253",
    "88.157.172.253"
]
result_dict1 = get_count_visits_from_ip(IP)
print(result_dict1)
result_dict2 = get_frequent_visit_from_ip(IP)
print(result_dict2)