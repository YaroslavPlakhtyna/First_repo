from datetime import datetime

class Note:
    def __init__(self, content):
        self.content = content
        self.timestamp = datetime.now()
        self.timestamp = (self.timestamp.strftime('%A %d %B %Y'))

def save_note(note, notes_list):
    notes_list.append(note)

# Приклад використання:

# Створюємо пустий список для зберігання нотаток
my_notes = []

# Створюємо нову нотатку
new_note_content = "Це моя перша нотатка."
new_note = Note(new_note_content)

# Зберігаємо нотатку
save_note(new_note, my_notes)

# Додаємо іншу нотатку
another_note_content = "Ще одна цікава думка."
another_note = Note(another_note_content)

# Зберігаємо іншу нотатку
save_note(another_note, my_notes)

# Виводимо всі нотатки
for note in my_notes:
    print(f"{note.timestamp}: {note.content}")