"""Для минулого завдання додамо клас Owner — власника собаки. 
У класу є три атрибути: ім'я — name, вік — age та адреса — address. 
Також необхідно реалізувати метод info, який повертає словник з ключами 'name', 'age' і 'address', 
та значення яких дорівнюють відповідним властивостям екземпляра класу.

Реалізувати для класу Dog атрибут owner, який буде екземпляром класу Owner.
Додати до класу Dog метод who_is_owner, який повертає результат виклику методу info екземпляра класу Owner, 
тобто це словник з ключами name, age та address власника."""
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {'name': self.name, 'age': self.age, 'address': self.address}


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner  # Додали атрибут owner, який є екземпляром класу Owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        # Викликаємо метод info для отримання інформації про власника
        return self.owner.info()

# Створюємо екземпляр класу Owner
owner = Owner("John Doe", 35, "123 Main St")

# Створюємо екземпляр класу Dog та передаємо власника
dog = Dog("Buddy", 25, "Golden Retriever", owner)

# Викликаємо метод who_is_owner для отримання інформації про власника собаки
print(dog.who_is_owner())  # Повинно вивести {'name': 'John Doe', 'age': 35, 'address': '123 Main St'}