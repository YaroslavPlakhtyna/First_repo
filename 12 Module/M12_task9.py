"""Реалізуйте метод __copy__ для класу Person.

Реалізуйте методи __copy__ та __deepcopy__ для класу Contacts."""

import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        # Створюємо новий об'єкт Person, використовуючи конструктор
        new_person = self.__class__(
            self.name,
            self.email,
            self.phone,
            self.favorite
        )
        return new_person

    def __deepcopy__(self, memo):
        # Глибоке копіювання використовуючи конструктор
        new_person = self.__class__(
            copy.deepcopy(self.name, memo),
            copy.deepcopy(self.email, memo),
            copy.deepcopy(self.phone, memo),
            copy.deepcopy(self.favorite, memo)
        )
        return new_person


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        # Поверхневе копіювання для класу Contacts
        new_contacts = self.__class__(
            self.filename,
            copy.copy(self.contacts)
        )
        return new_contacts

    def __deepcopy__(self, memo):
        # Глибоке копіювання для класу Contacts
        new_contacts = self.__class__(
            self.filename,
            copy.deepcopy(self.contacts, memo)
        )
        return new_contacts