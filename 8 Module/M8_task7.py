"""У нас є іменований кортеж для зберігання котів у змінній Cat.
На першому місці у нас кличка котика nickname, потім його вік age та ім'я власника кота owner.

Напишіть функцію convert_list(cats), яка працюватиме у двох режимах.

Якщо функція convert_list приймає у параметрі cats список іменованих кортежів

[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
То функція поверне наступний список словників:

[
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
І в той же час, якщо функція convert_list приймає в параметрі cats список словників, 
то результатом буде зворотна операція та функція поверне список іменованих кортежів.

Для визначення типу параметра cats використовуйте функцію isinstance."""

import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"]) # Визначення іменованого кортежу Cat

def convert_list(cats):
    result = []

    for cat in cats:
        if isinstance(cat, Cat):
            result.append({"nickname": cat.nickname, "age": cat.age, "owner": cat.owner})
        else:
            result.append(Cat(cat['nickname'], cat['age'], cat['owner']))

    return result

# У циклі for функція перевіряє кожен елемент у вхідному списку cats. Якщо елемент є іменованим кортежем Cat, то функція додає в результуючий список словник, створений з полів іменованого кортежу. Якщо елемент є словником, то функція додає в результуючий список іменований кортеж Cat, створений з полів словника. Функція повертає результуючий список.
# Цей підхід дозволяє конвертувати дані між представленням іменованих кортежів та словників, що може бути зручним у різних ситуаціях програмування.


# Приклад використання
cats_namedtuple = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
cats_dict = [
    {'nickname': 'Mick', 'age': 5, 'owner': 'Sara'},
    {'nickname': 'Barsik', 'age': 7, 'owner': 'Olga'},
    {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}
]

result_dict = convert_list(cats_namedtuple)
result_namedtuple = convert_list(cats_dict)

print(result_dict)
print(result_namedtuple)