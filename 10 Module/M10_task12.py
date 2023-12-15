"""Створіть клас IDException, який успадковуватиме клас Exception.

Також реалізуйте функцію add_id(id_list, employee_id), 
яка додає до списку id_list ідентифікатор користувача employee_id та повертає вказаний оновлений список id_list.

Функція add_id буде викликати власне виключення IDException, якщо employee_id не починається з '01', 
інакше employee_id буде додано до списку id_list."""

class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException("Invalid employee ID format. It should start with '01'.")
    id_list.append(employee_id)
    return id_list

#You can use this function as follows:

# Example usage
ids = ['0101', '0123', '0145']

try:
    new_ids = add_id(ids, '0189')
    print("Updated IDs:", new_ids)
except IDException as e:
    print(f"Error: {e}")
        