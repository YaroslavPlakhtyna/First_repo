"""Завдання 1
На першому етапі вам потрібно реалізувати функцію для виведення списку колег, яких потрібно привітати з днем народження на тижні.

У вас є список словників users, кожен словник у ньому обов'язково має ключі name та birthday. 
Така структура представляє модель списку користувачів з їх іменами та днями народження. Де name — це рядок з ім'ям користувача,
а birthday — це datetime об'єкт, в якому записаний день народження.

Наприклад:

{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}

Ваше завдання написати функцію get_birthdays_per_week, яка отримує на вхід список users і виводить у консоль (за допомогою print)
список користувачів, яких потрібно привітати по днях на наступному тижні.

Рекомендації для виконання
Давайте розберемо покроковий план алгоритму для пошуку днів народження протягом наступного тижня

Підготовка Даних: Перш ніж почати обчислення, потрібно зібрати відомості про користувачів. Ми очікуємо,
в аргументі функції get_birthdays_per_week список словників users, де кожен словник містить ім'я та дату народження користувача.
Як варіант, ми можемо зберігати дні народження необхідних користувачів в наступній структурі даних
{'Monday': ['Bill Gates'], 'Thursday': ['Jan Koum']}

Для цього ми можемо наприклад використати `defaultdict(list)`

Отримання Поточної Дати: Отримуємо поточну дату системи для подальшого порівняння з датами народження користувачів datetime.today().date().
Перебір Користувачів: Проходимо по списку користувачів та аналізуємо їх дати народження `for user in users:`.
В середині циклу for проводимо аналіз дати народження: 
a. Конвертація Дати: Конвертуємо час народження до типу date, видаляючи часову частину.
name = user["name"]
birthday = user["birthday"].date()  *# Конвертуємо до типу date*
birthday_this_year = birthday.replace(year=today.year)

b. Оцінка Дати на Цей Рік : Перевіряємо, чи вже минув день народження цього року if birthday_this_year < today.
Якщо так, то розглядаємо дату на наступний рік, це треба у birthday_this_year використовуючи метод replace збільшити рік на одиничку.
c. Порівняння з Поточною Датою: Визначаємо різницю між днем народження та поточним днем,
щоб знайти дні народження на тиждень вперед delta_days = (birthday_this_year - today).days.

d. Визначення Дня Тижня: Визначаємо день тижня дня народження. Якщо це вихідний, переносимо на понеділок.
Тут треба подивитись, щоб delta_days < 7, перед тим як визначити на який день ставимо поздоровлення.

Зберігання Результату : Зберігаємо ім'я користувача в відповідний день тижня, якщо день народження відбувається протягом наступного тижня.
Виведення Результату: Виводимо зібрані імена по днях тижня у відповідному форматі.

Критерії оцінювання
- Функція get_birthdays_per_week виводить імена іменинників у форматі:
Monday: Bill Gates, Jill Valentine
Friday: Kim Kardashian, Jan Koum

- Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.
- Функція виводить користувачів з днями народження на тиждень вперед від поточного дня.
- Тиждень починається з понеділка."""

from datetime import datetime, timedelta
from collections import defaultdict

users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
         {"name": "Volodya", "birthday": datetime(1989, 12, 12)},
         {"name": "Dad", "birthday": datetime(1959, 12, 16)},
         {"name": "Mum", "birthday": datetime(1960, 12, 17)},
         {"name": "Vlad", "birthday": datetime(1991, 12, 14)},
         {"name": "Andrii", "birthday": datetime(1990, 12, 15)},
         {"name": "Oleh", "birthday": datetime(year=1999, month=9, day=12)}
         ]

def get_birthdays_per_week(users:list[dict]):
    contacts = defaultdict(list)
    print(f'{contacts=}')
    today = datetime.today().date()
    print(f'{today=}')
    for user in users:
        print(f'{user=}')
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date
        birthday_this_year = birthday.replace(year=today.year)
        print(f'{name=} {birthday_this_year=}')
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            print(f'{birthday_this_year}')
            
        delta_days = (birthday_this_year - today).days
        print(f'{delta_days=}')
        if delta_days <= 7:
            birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")
            print(f'{birthday_weekday=}')
            if birthday_weekday in ['Sunday','Saturday']:
                birthday_weekday = 'Next Monday'
            contacts[birthday_weekday].append(name)
    print(f'{contacts=}')
    info = ''
    tail = ''
    for k, value in contacts.items():
        if k == 'Next Monday':
            tail += f"{k}: {', '.join(value)}"
            continue
        info += f"{k}: {', '.join(value)}\n"
    info += tail 
    print(info)


get_birthdays_per_week(users)
