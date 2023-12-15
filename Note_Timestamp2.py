from datetime import datetime

class Note:
    def __init__(self, content):
        self.content = content
        self.timestamp = datetime.now()

class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, content):
        new_note = Note(content)
        self.notes.append(new_note)

    def search_notes(self, keyword):
        return [note for note in self.notes if keyword.lower() in note.content.lower()]

    def edit_note(self, note_index, new_content):
        if 0 <= note_index < len(self.notes):
            self.notes[note_index].content = new_content

    def delete_note(self, note_index):
        if 0 <= note_index < len(self.notes):
            del self.notes[note_index]

    def show_all_notes(self):
        for i, note in enumerate(self.notes):
            print(f"{i + 1}. {note.timestamp}: {note.content}")

# Приклад використання:

notes_manager = NotesManager()

# Додаємо нові нотатки
notes_manager.add_note("Перша нотатка.")
notes_manager.add_note("Друга нотатка.")
notes_manager.add_note("Третя нотатка.")

# Показуємо всі нотатки
print("Всі нотатки:")
notes_manager.show_all_notes()

# Шукаємо нотатки, які містять слово "друга"
search_result = notes_manager.search_notes("друга")
print(f"\nРезультат пошуку: {search_result}")

# Редагуємо другу нотатку
notes_manager.edit_note(1, "Відредагована нотатка.")
print("\nНотатка після редагування:")
notes_manager.show_all_notes()

# Видаляємо першу нотатку
notes_manager.delete_note(0)
print("\nНотатка після видалення:")
notes_manager.show_all_notes()