"""Напишіть функцію parse_folder, вона приймає єдиний параметр path,
який є об'єктом Path. Функція повинна просканувати директорію path та повернути кортеж із двох списків.
Перший — це список файлів усередині директорії, другий — список директорій.

Приклад виводу функції:

(['.gitignore', 'readme.md'],
 ['.git', '.idea', '.vscode', 'module-01', 'module-02', 'module-03', 'module-04', 'module-05', 
 'module-06', 'module-07', 'module-08', 'module-09', 'module-10', 'module-11', 'module-12'])"""

from pathlib import Path

def parse_folder(path):
    p = path    
    files = []
    folders = []
    for item in p.iterdir():
        if item.is_file():
            files.append(item.name) #В цьому випадку item.name використовується для додавання тільки імені файлу до списку files.
            print(files)
        elif item.is_dir():
            folders.append(item.name) #В цьому випадку item.name використовується для додавання тільки імені файлу до списку folders.
            print(folders)

    return files, folders