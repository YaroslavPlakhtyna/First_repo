"""Концепцію замикання може добре пояснити приклад кешування значень функції.

Підсумкове завдання модуля 3 було — рекурсивне обчислення чисел Фібоначчі.

Ряд Фібоначчі - це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ..., 
де кожне наступне число послідовності виходить додаванням двох попередніх членів ряду.

У загальному вигляді для обчислення n-го члена ряду Фібоначчі потрібно вирахувати вираз: Fn = Fn-1 + Fn-2.

Це завдання можна вирішити рекурсивно, викликаючи функцію, що обчислює числа послідовності доти, 
доки виклик не сягне членів ряду менше n = 1, де послідовність задана.

Створіть функцію caching_fibonacci(), яка матиме кеш із попередньо обчисленими значеннями чисел Фібоначі. 
Усередині вона містить функцію fibonacci(n), яка безпосередньо і обчислюватиме саме число Фібоначчі. 
Функція caching_fibonacci() повертає функцію fibonacci

Якщо число Фібоначчі зберігається у словнику cache, то функція fibonacci повертає число з кеша. 
Якщо його немає у кеші, то ми обчислюємо число і поміщаємо його в кеш, і повертаємо з функції fibonacci."""
def caching_fibonacci():
    # Кеш для зберігання попередньо обчислених значень чисел Фібоначі
    cache = {}

    # Внутрішня функція для обчислення чисел Фібоначі
    def fibonacci(n):
        # Перевірка, чи число вже є в кеші
        if n in cache:
            return cache[n]

        # Базовий випадок для завершення рекурсії
        if n <= 1:
            return n

        # Рекурсивний виклик для обчислення чисел Фібоначі
        result = fibonacci(n - 1) + fibonacci(n - 2)

        # Зберігаємо результат в кеші
        cache[n] = result

        return result

    # Повертаємо функцію fibonacci
    return fibonacci

# Приклад використання:
fibonacci_func = caching_fibonacci()

# Обчислення чисел Фібоначі з використанням кешу
result1 = fibonacci_func(5)
result2 = fibonacci_func(8)
result3 = fibonacci_func(10)

print(f"Fibonacci(5): {result1}")
print(f"Fibonacci(8): {result2}")
print(f"Fibonacci(10): {result3}")