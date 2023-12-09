"""Розробіть функцію sanitize_file(source, output),
що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

Вимоги:

- прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
- запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with
та режим "w"
- запис нового вмісту файлу output має бути одноразовий і використовувати метод write"""

def sanitize_file(source, output):
    with open(source, 'r') as fh:
        for line in fh:
            no_digit_line = ''.join(i for i in line if not i.isdigit())
            with open(output, 'w') as fh:
                for line in fh:
                    new_line = fh.write(no_digit_line)
                return new_line
