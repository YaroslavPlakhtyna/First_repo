"""При аналізі даних часто виникає необхідність позбавитися екстремальних значень,
перш ніж почати працювати з даними далі. Напишіть функцію prepare_data,
яка видаляє з переданого списку найбільше та найменше значення,
сортує його в порядку зростання і повертає змінений список як результат."""

# 1. sort -> remove MAX and MIN numbers -> return result

def prepare_data(data):
    new_data = sorted(data)
    new_data.remove(max(data))
    new_data.remove(min(data))
    return new_data
print(prepare_data([1, -3, 4, 100, 0, -5, 10, 1, 1]))