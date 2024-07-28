from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QTextEdit, 
    QLabel,
    QListWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout)

import json

app = QApplication([])
win = QWidget()

### Создание виджетов
textarea = QTextEdit()
textarea.setPlaceholderText('Введите текст заметки:')
note_text = QLabel('Список заметок')
notes_list = QListWidget()


btn_create = QPushButton('Создать заметку')
btn_delete = QPushButton('Удалить заметку')
btn_save = QPushButton('Сохранить заметку')










### Расположение виджетов по линиям
main_line = QHBoxLayout()
left_line = QVBoxLayout()
right_line = QVBoxLayout()
btn_line = QHBoxLayout()

# Маленькая
btn_line.addWidget(btn_create)
btn_line.addWidget(btn_delete)

# Левая
left_line.addWidget(textarea)

# Правая
right_line.addWidget(note_text)
right_line.addWidget(notes_list)
right_line.addLayout(btn_line)
right_line.addWidget(btn_save)

# Главная
main_line.addLayout(left_line)
main_line.addLayout(right_line)
win.setLayout(main_line)

# чтение файла с заметками
with open ("notes.json", "r", encoding="utf-8") as file:
    notes_data = json.load(file)
    print(notes_data)

# Функциональный блок
def show_note():
    textarea.setText(notes_data[notes_list.currentItem().text()]['текст'])


# показывание окна и запуск приложения
notes_list.addItems(notes_data.keys())
notes_list.itemClicked.connect(show_note)

win.show()
app.exec()
