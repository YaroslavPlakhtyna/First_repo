"""Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою
по кожному розробнику компанії.

Приклад файлу:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати,
розділеної комою.

Розробіть функцію total_salary(path) (параметр path - шлях до файлу),
яка буде розбирати текстовий файл і повертати загальну суму заробітної плати всіх розробників компанії.

Вимоги до завдання:

функція total_salary повертає значення типу float
для читання файлу функція total_salary використовує лише метод readline
ми поки що не використовуємо менеджер контексту with"""

def total_salary(path):
    total = 0

    # Відкриваємо файл
    file = open(path, 'r')

    try:
        line = file.readline()
        while line:
            parts = line.split(',')
            total += float(parts[1])
            line = file.readline()
    finally:
        # Вручну закриваємо файл у випадку будь-яких помилок
        file.close()

    return total

# У зразку коду, який я вам надав (нижче), використовується with open(...) as file. 
# В контекстному менеджері with, файл буде автоматично закритий при завершенні блоку with.
# Отже, вам не потрібно явно викликати метод close().
# Цей підхід є безпечнішим і зручнішим, оскільки гарантує, що ресурс (у цьому випадку файл)
# буде коректно закритий, навіть якщо виникне виняток під час виконання блоку with.

def total_salary(path):
    # Ініціалізуємо загальну суму
    total = 0

    # Відкриваємо файл за заданим шляхом
    with open(path, 'r') as file:
        # Читаємо файл рядок за рядком
        line = file.readline()
        while line:
            # Розділяємо рядок за комою на ім'я та заробітну плату
            parts = line.split(',')
            
            # Додаємо заробітну плату до загальної суми
            total += float(parts[1])
            
            # Читаємо наступний рядок
            line = file.readline()

    # Повертаємо загальну суму
    return total

# Приклад використання
file_path = 'шлях_до_вашого_файлу.txt'
result = total_salary(file_path)
print(f"Загальна сума заробітної плати: {result}")