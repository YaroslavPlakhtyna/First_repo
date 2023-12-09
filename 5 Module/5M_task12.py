"""У шостій задачі ми писали функцію is_spam_words, яка визначала,
чи є чи ні стоп-слова у тексті повідомлення.
Підемо далі та застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон. 
Наприклад, всі "погані" слова замінюватимемо зірочками.
Напишіть функцію replace_spam_words, яка приймає рядок (параметр text),
перевіряє його на вміст заборонених слів зі списку (параметр spam_words),
та повертає результат рядок, але замість заборонених слів, підставлений шаблон з *,
причому довжина шаблону дорівнює довжині забороненого слова.
Визначити нечутливість до регістру стоп-слів."""

import re


def replace_spam_words(text, spam_words):
    for spam_word in spam_words:
        # Create a pattern for matching the spam word (case-insensitive)
        pattern = re.compile(re.escape(spam_word), flags=re.IGNORECASE)

        # Create a replacement string with asterisks of the same length as the spam word
        replacement = '*' * len(spam_word)

        # Use re.sub to replace occurrences of the spam word with the asterisk pattern
        text = re.sub(pattern, replacement, text)

    return text