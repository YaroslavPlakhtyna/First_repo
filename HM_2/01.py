"""Завдання 1
Доробіть консольного бота помічника та додайте обробку помилок.

Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
Цей декоратор відповідає за повернення користувачеві повідомлень типу 
"Enter user name", "Give me name and phone please" тощо. 
Декоратор input_error повинен обробляти винятки, 
що виникають у функціях - handler (KeyError, ValueError, IndexError) 
та повертати відповідну відповідь користувачеві.

Додамо декоратор input_error для обробки помилки ValueError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

Та обгорнемо декоратором функцію add_contact нашого бота, щоб ми почали обробляти помилку ValueError.

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

Вам треба додати обробники до інших команд, та додати в декоратор обробку винятків інших типів. 
Бажаємо успіху при виконані домашнього завдання.
"""

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "You should write 2 values"
        except KeyError:
            return "Contact not found, please add contact."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    print(f'{contacts=}')
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args[0], args[1]
    if name in contacts.keys():
        contacts[name] = phone
        print(f'{contacts=}')
        return "Contact changed."
    else:
        return "Contact not found, please add contact."

@input_error
def show_contact(args, contacts):
    name = args[0]
    phone = contacts[name]
    return phone 
# TODO: Need to remove
#    for key, value in contacts.items():
#        if key == name:
#            return value
#    return "Contact not found, please add contact." 

def show_all_contact(contacts):
    info = ""
    for name, phone in contacts.items():
        info += f'{name}: {phone}\n'
    return info

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        print(f'{command=}, {args}')
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))   
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(show_all_contact(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()