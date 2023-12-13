"""Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме вміст файлу,
додаватиме до прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.

Кожний рядок у створеному файлі повинен починатися з його номера, двокрапки та пробілу,
після чого має йти текст рядка з вхідного файлу.

Нумерація рядків іде від 0."""

def to_indexed(source_file, output_file):
    with open(source_file, 'r') as source:
        lines = source.readlines()

    with open(output_file, 'w') as output:
        for i, line in enumerate(lines):
            output.write(f"{i}: {line}")