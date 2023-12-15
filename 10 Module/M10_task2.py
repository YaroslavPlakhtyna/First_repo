"""Створіть клас Animal. Також створіть екземпляр класу Animal та привласніть змінній animal. 
Для класу Animal у конструкторі створіть дві властивості: nickname - кличка тварини та weight - вага тварини.
Реалізуйте також метод класу say. 
При реалізації методу можна використати оператор pass, поки що головне - це визн"""

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return f"Hi {self.nickname}"

a = Animal("Siri", 10)
    