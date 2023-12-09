"""Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок Азії.
Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .

Компанія працює з наступними країнами:

Країна	    Код ISO	    Префікс
Japan	    JP	        +81
Singapore	SG	        +65
Taiwan	    TW	        +886
Ukraine 	UA	        +380
Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних номерів.

Напишіть функцію get_phone_numbers_for_сountries, яка буде:

Приймати список телефонних номерів.
Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
Сортувати телефонні номери за вказаними у таблиці країнами.
Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}
Якщо не вдалося порівняти код телефону з відомими,
цей телефон повинен бути доданий до списку словника з ключем 'UA'."""

def sanitize_phone_number(phone):
    result = ""
    remove_chars = "(, -, ), +"
    for char in phone:
        if char not in remove_chars:
            result += char
    return result.strip()


def get_phone_numbers_for_countries(list_phones):
    # Define country codes and their corresponding prefixes
    country_code = {
    "JP": "81",
    "SG": "65",
    "TW": "886",
    "UA": "380"
    }
    normalized_numbers = [] # Define an empty list to store normalized phone numbers
    for phone in list_phones: # Iterate over each phone number in the list_phones
        normalized_numbers.append(sanitize_phone_number(phone)) # Call the sanitize_phone_number function on each phone number and append the result to the normalized_numbers list
    phone_numbers_by_country = {}
    for code in country_code.keys():
        phone_numbers_by_country[code] = []
    for number in normalized_numbers:
        matched_country = None
        for code, prefix in country_code.items():
            if number.startswith(prefix):
                matched_country = code
                break
        if matched_country:
            phone_numbers_by_country[matched_country].append(number)
        else:
            # If no match is found, add the number to the default "UA" category
            phone_numbers_by_country["UA"].append(number)
    return phone_numbers_by_country

list_phones = "+818765347, +8867658976"
result = get_phone_numbers_for_countries([list_phones])
print(result) 