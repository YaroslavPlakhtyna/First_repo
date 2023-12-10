# module 6 2:35:10
"""Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список,
виконує кодування кожної пари username:password у формат Base64 та повертає список із закодованими парами username:password у вигляді:

['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']"""



import base64
def encode_data_to_base64(data):
    result = []
    for user in data:
        user_bytes = user.encode()
        base64_bytes= base64.b64encode(user_bytes)
        result.append(base64_bytes.decode())
    return result