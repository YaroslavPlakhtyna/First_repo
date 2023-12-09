"""Другий етап. 
Необхідно написати функцію is_valid_password, яка перевірятиме отриманий параметр — пароль на надійність.

Критерії надійного пароля:

Довжина рядка пароля вісім символів.
Містить хоча б одну літеру у верхньому регістрі.
Містить хоча б одну літеру у нижньому регістрі.
Містить хоча б одну цифру.
Функція is_valid_password повинна повернути True, 
якщо переданий параметр пароль відповідає вимогам на надійність. Інакше повернути False."""

def is_valid_password(password):
    if len(password) != 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True
                

