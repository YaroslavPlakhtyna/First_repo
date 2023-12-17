"""У класу Point через конструктор __init__ оголошено два атрибути: координати x та y.
Приховати доступ до них з допомогою подвійного підкреслення: __x та __y

Реалізуйте для класу Point механізми setter та getter до атрибутів __x та __y 
за допомогою декораторів property та setter.

Приклад:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10
"""

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

# Приклад використання:

point = Point(1, 2)

# Використовуємо getter для x та y
print(f"x: {point.x}, y: {point.y}")

# Використовуємо setter для x та y
point.x = 10
point.y = 20

# Перевіряємо, що зміни відбулися
print(f"New values: x: {point.x}, y: {point.y}")