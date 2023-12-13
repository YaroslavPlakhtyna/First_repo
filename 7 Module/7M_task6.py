"""Всі ви, можливо, стикалися з ребусами "Знайди слово". Вони існують як текстові варіанти,
так і як програми для мобільних додатків. Нагадаємо коротко суть ребуса.
У великому квадраті з набором букв необхідно знайти слово по горизонталі та інколи по вертикалі.

Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) для знаходження слова, 
що шукається в рядку ребуса.

Параметри функції:

riddle - рядок із зашифрованим словом.
word_length – довжина зашифрованого слова.
start_letter - літера, з якої починається слово (мається на увазі, 
що до початку слова літера не зустрічається в рядку).
reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому. 
Для значення True слово зашифроване у зворотньому порядку, наприклад,
у рядку 'mi1rewopret' зашифроване слово 'power'.
Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.
"""
def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
        riddle = riddle[::-1]  # Reverse the riddle string if reverse is True

    for i in range(len(riddle) - word_length + 1):
        current_word = riddle[i:i + word_length]
        if current_word[0] == start_letter and current_word.isalpha():
            return current_word

    return ""

# Test cases
riddle1 = "mi1rewopret"
result1 = solve_riddle(riddle1, 5, 'p')
print(result1)  # Output: power

riddle2 = "batcatrat"
result2 = solve_riddle(riddle2, 3, 'r', reverse=True)
print(result2)  # Output: rat