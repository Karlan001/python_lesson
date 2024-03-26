# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.
import datetime
import json
import random


def add_notes(note):
    uuid = ""
    for i in range(4):
        uuid += str(random.randrange(1, 10))
    note["UUID"] = uuid
    note["Вермя добавления заметки"] = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    with open('notes.json', 'a', ) as fileWrite:
        fileWrite.write(json.dumps(note, ensure_ascii=False, ) + '\n')
        

def create_note():
    head = input("Введите тему заметки: ")
    body = input("Введите содержание заметки: ")
    result = dict()
    result[f"Тема {head}"] = f"Тело {body}"
    return dict(result)

def show_all():
    with open('notes.json', 'r') as file:
        print(file.read())

def search_note():
    search = input("Введите тему или UUID заметки для поиска: ")
    with open('notes.json', "r", encoding="utf-8") as notes_file:
        data = [json.loads(jline) for jline in notes_file]
        for v in data:
            for key in dict(v).keys():
                if key == f"Тема {search}":
                    print(v)
                    return(v)
                else: print("Заметки по указанной теме нет")
            for values in dict(v).values():
                if values == search:
                    print(v)
                    return(v)
                else: print("Заметки по указанному UUID нет")

def deletedNote():
    search = input("Введите тему заметки для удаления: ")
    deleted = 0
    with open('notes.json', "r", encoding="utf-8") as notes_file:
        data = [[json.loads(jline)] for jline in notes_file]
        for i in range(len(data)):
            for key in dict(*data[i]).keys():
                if f"Тема {search}" == key:
                    deleted = i
                else: print("Заметки по указанной теме нет")
        data.pop(deleted)
    with open('notes.json', 'w+', ) as fileWrite:
        for i in data:
            fileWrite.write(json.dumps(*i, ensure_ascii=False, ) + '\n')

def changeNote():
    fordel = dict(search_note())
    tema = ""
    for i in fordel:
        if "Тема" in i:
            tema = i
        else: print("Такой темы не найдено")
    search = tema
    deleted = 0
    with open('notes.json', "r", encoding="utf-8") as notes_file:
        data = [[json.loads(jline)] for jline in notes_file]
        for i in range(len(data)):
            for key in dict(*data[i]).keys():
                if search == key:
                    deleted = i
        data.pop(deleted)
    with open('notes.json', 'w+', ) as fileWrite:
        for i in data:
            fileWrite.write(json.dumps(*i, ensure_ascii=False, ) + '\n')
    add_notes(create_note())