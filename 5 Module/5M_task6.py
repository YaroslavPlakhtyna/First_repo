"""Розглянемо завдання на перевірку спаму в електронному листі або фільтрацію заборонених слів
у повідомленні.
Нехай функція is_spam_words приймає рядок (параметр text), перевіряє його на вміст
заборонених слів зі списку (параметр spam_words), і повертає результат перевірки:
True, якщо є хоч одне слово присутнє зі списку, та False, якщо в тексті стоп-слів не виявлено.

Слова у параметрі text можуть бути у довільному регістрі, а значить функція is_spam_words,
при пошуку заборонених слів, регістру незалежна і весь текст має зводитися до нижнього регістру.
Для спрощення, будемо вважати, що в рядку є тільки одне заборонене слово.

Передбачити третій параметр функції space_around, який за замовчуванням дорівнює False.
Він відповідатиме за те, що функція шукатиме окреме слово чи ні. Слово вважати, що стоїть окремо,
якщо ліворуч від слова знаходиться символ пробілу або воно розташоване на початку тексту,
а праворуч від слова знаходиться пробіл або символ крапки.

Наприклад, у тексті ми шукаємо слово "лоток". То в слові "молоток" виклик та результат буде наступним:

print(is_spam_words("У діда в руках молоток.", ["лоток"]))  # True
print(is_spam_words("У діда в руках молоток.", ["лоток"], True))  # False
Тобто у другому випадку слово не окреме і є частиною іншого.

У цьому прикладі функція поверне True в обох випадках.

print(is_spam_words("У кота порожній лоток.", ["лоток"]))  # True
print(is_spam_words("У кота порожній лоток.", ["лоток"], True))  # True
"""

def is_spam_words(text, spam_words, space_around=False):
    if space_around:
        text = f" {text} "
    lower_text = text.lower()
    for spam_words in spam_words:
        if space_around:
            spam_word = f" {spam_words} "
        lower_spam_word = spam_words.lower()
        if lower_spam_word in lower_text:
            return True
    return False


print(is_spam_words('You’re decent, but you seem like a mismatch.', ['match'], True))

    
        