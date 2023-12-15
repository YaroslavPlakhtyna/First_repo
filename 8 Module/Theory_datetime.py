from datetime import datetime

#Щоб отримати поточну дату і час без урахування часового пояса, можна викликати метод now() у datetime:
current_datetime = datetime.now()
print(current_datetime)

#У результаті виклику now() ми отримуємо об'єкт datetime, у якого є ряд корисних атрибутів:
print(current_datetime.year)       
print(current_datetime.month)     
print(current_datetime.day)       
print(current_datetime.hour)       
print(current_datetime.minute)     
print(current_datetime.second)     
print(current_datetime.microsecond)

#В об'єкта datetime є методи, щоб отримати дату (без часу) та час (без дати):
print(current_datetime.date()) 
print(current_datetime.time()) 

#Щоб створити об'єкт datetime з будь-якою вибраною датою, можна зробити так:
d1 = datetime(year=2012, month=1, day=7, hour=14)
print(d1) # 2012-01-07 14:00:00

#Щоб дізнатися день тижня, можна скористатися методом weekday:
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
print(seventh_day_2020.weekday()) 

# Щоб порівняти два об'єкти datetime, достатньо скористатися оператором порівняння:
current_datetime = datetime.now()

future_month = (current_datetime.month % 12) + 1
future_year = current_datetime.year + int(current_datetime.month / 12)
future_datetime = datetime(future_year, future_month, 1)

print(current_datetime < future_datetime) 

#Якщо відняти від одного datetime об'єкту інший, то отримаємо timedelta об'єкт.
# Він відповідає за відрізок часу між двома датами.
seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)                   # 365 days, 0:00:00
print(difference.total_seconds())   # 31536000.0

#Об'єкти timedelta можна створювати самостійно, щоб отримати дату/час віддалену від початкової:
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)   # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)   # 2019-12-10 14:00:00

#Об'єкт timedelta можна створити, задаючи тижні, дні, години, хвилини, секунди, мілісекунди і мікросекунди:
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)

#Звичайно можна з timestamp отримати дату/час і навпаки:
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
ts = seventh_day_2020.timestamp()
print(ts)   # 1578398400.0

ts += 100_000
print(datetime.fromtimestamp(ts))   # 2020-01-08 17:46:40

#Коли потрібно перетворити дату/час в рядок, ви можете скористатися функцією str, яка перетворить datetime у рядок. 
#Але часто формат такого перетворення незручний і в Python є окрема мінімова для опису, як перетворити дату/час в рядок:
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
print(seventh_day_2020.strftime('%A %d %B %Y')) # Tuesday 07 January 2020

#Та ж міні-мова використовується для конвертації вже рядків в дату/час:
s = '10 January 2020'
print(datetime.strptime(s, '%d %B %Y')) # 2020-01-10 00:00:00