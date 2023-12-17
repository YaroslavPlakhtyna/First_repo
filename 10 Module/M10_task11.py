"""Створіть клас NumberString, успадкуйте його від класу UserString,
визначте для нього метод number_count(self), який буде рахувати кількість цифр у рядку."""

from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = sum(char.isdigit() for char in self.data)
        return count
    
string_instance = NumberString("abc123xyz456")
result = string_instance.number_count()

print(result)
        