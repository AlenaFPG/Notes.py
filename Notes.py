class Note:
    def __init__(self, title, content, creation_date):
        self.title = title
        self.content = content
        self.creation_date = creation_date

import json

class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []

    def load_notes(self):
        with open(self.file_path, 'r') as file:
            self.notes = json.load(file)

    def save_notes(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.notes, file)

    def add_note(self, note):
        self.notes.append(note)

    def edit_note(self, note_index, new_title, new_content):
        self.notes[note_index].title = new_title
        self.notes[note_index].content = new_content

    def delete_note(self, note_index):
        del self.notes[note_index]

    if __name__ == "__main__":

        while True:
            print('Выберите дейтсиве: ')
            print('1. Создать заметку')
            print('2. Читать список заметов')
            print('3. Редактировать заметку')
            print('4. Удалить заметку')
            print('5. Выйти')

            выбор = input('Введите номер действия: ')

            if выбор == '1':
                title = input('Введите заголовок заметки: ')
                content = input('Введите содержание заметки: ')
                note = Note(title, content)
                note.save_notes()
                print('Заметка успешно создана')

            elif выбор == '2':
                notes = Note.load_notes()
                if notes:
                    print('Список заметок: ')
                    for i, note in enumerate(notes, 1):
                        print(f'{i}. {note.title}')
                else:
                    print('Нет ни одной заметки')

            elif выбор == '3':
                title = input('Введите заголовок заметки, которую нужно отредактировать: ')
                new_content = input('Введите новое содержание заметки: ')
                Note.edit_note(title, new_content)
                print('Заметка успешно отредактирована')

            elif выбор == '4':
                title = input('Введите заголовок заметки, которую нужно удалить: ')
                Note.delete_note(title)
                print('Заметка успешно удалена')

            elif выбор == '5':
                break

            else:
                print('Неверный выбор')