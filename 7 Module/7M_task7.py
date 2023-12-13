"""У четвертому модулі розв'язували завдання нормалізації даних. Розширимо її.

При аналізі даних часто виникає необхідність позбавитися екстремальних значень,
перш ніж почати працювати з даними далі. Напишіть функцію data_preparation, яка приймає набір даних,
список списків (Приклад: [[1,2,3],[3,4], [5,6]]).

Функція повинна видаляти з переданих списків найбільше і найменше значення,
але якщо розмір списку понад два елементи.
Після видалення даних з кожного списку необхідно злити їх разом в один список,
відсортувати його за зменшенням та повернути отриманий список як результат
(Для прикладу вище результат буде наступним: [6, 5, 4, 3, 2])."""
def data_preparation(list_data): 
    combined_list = []

    for sublist in list_data:
        combined_list = []

    for sublist in list_data:
        if len(sublist) > 2:
            sublist.remove(max(sublist))
            sublist.remove(min(sublist))
        combined_list.extend(sublist)
    return sorted(combined_list, reverse=True)


input_data = [[1,2,3], [3,4], [5,6]]
result = data_preparation(input_data)
print(result)