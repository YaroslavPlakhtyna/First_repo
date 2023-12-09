"""Напишіть функцію find_word, яка приймає два параметри: перший text та другий word.
Функція виконує пошук зазначеного слова word у тексті text за допомогою функції search та
повертає словник.

При виклику функції:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))
Результат має бути наступного виду при збігу:

{
    'result': True,
    'first_index': 34,
    'last_index': 40,
    'search_string': 'Python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}
де

result — результат пошуку True або False
first_index — початкова позиція збігу
last_index — кінцева позиція збігу
search_string — частина рядка, в якому був збіг
string — рядок, переданий у функцію
Якщо збігів не виявлено:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "python"))
Результат:

{
    'result': False,
    'first_index': None,
    'last_index': None,
    'search_string': 'python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}"""

import re


def find_word(text, word):
    result = re.search(word, text)
    # Check if the word was found
    if result:
        # Extract relevant information from the search result
        first_index, last_index = result.span()
        found_string = result.group()

        # Create a dictionary with the result details
        result_dict = {
            'result': True,
            'first_index': first_index,
            'last_index': last_index - 1,  # Adjust the last index to match the example
            'search_string': word,
            'string': text
        }
    else:
        # If the word was not found, create a dictionary indicating the result is False
        result_dict = {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        }

    return result_dict

print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "python"))

"""In this implementation:

We use the search function to find the word in the text.
If the word is found, we extract the start and end indices of the match, as well as the actual matched string.
We create a dictionary (result_dict) with the relevant information, including the result status, indices, search string, and the original text.
If the word is not found, we create a dictionary with the result set to False.
This approach uses the re module for regular expression search, assuming that's the search function you are using. Adjustments may be needed based on the actual implementation of your search function."""
