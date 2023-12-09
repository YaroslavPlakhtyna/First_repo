"""
Напишімо функцію, яка повертає повне ім'я користувача. 
У базі даних переважно зберігають ім'я користувача first_name, його прізвище last_name та по батькові,
або, як заведено в західних країнах, друге ім'я — middle_name.
Причому middle_name — це необов'язкова змінна, вона може бути,
а може й не передаватися під час виклику функції.
Наша функція повертатиме рядок з повним ім'ям 'first_name middle_name last_name',
якщо ж змінна middle_name відсутня, то рядок, що повертається повинен бути 'first_name last_name'.
"""


def get_fullname(first_name, last_name, middle_name=""):
    if first_name and middle_name and last_name:
        return(f"{first_name} {middle_name} {last_name}")
    return (f"{first_name} {last_name}")