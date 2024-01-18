# 1) Создать телефонный справочник: +++++
# - Открыть файл в режиме добавления (a) +++
# 2) Добавить контакт: +++++
# - Запросить информацию у пользователя +++
# - Подготовить данные в необходимом формате +++
# - Открыть файл в режиме добавления (a) +++
# - Добавить контакт в файл +++
# 3) Вывести данные из файла на экран: +++++
# - Открыть файл в режиме чтения (r) +++
# - Вывести информацию на экран +++
# 4) Поиск данных: +++++
# - Запросить вариант поиска +++
# - Запросить данные поиска +++
# - Открыть файл в режиме чтения (r) +++
# - Сохранить данные в переменную +++
# - Осуществить поиск по файлу +++
# - Вывести нужную информацию на экран +++
# 5) Реализовать UI: +++++
# - Вывести варианты меню +++
# - Получение запроса пользователя +++
# - Реализация запроса пользователя +++
# - Выход из программы +++

def input_name():
    return input('Введите имя: ')

def input_surname():
    return input('Введите фамилию: ')

def input_patronymic():
    return input('Введите отчество: ')

def input_phone():
    return input('Введите номер телефона: ')

def input_address():
    return input('Введите адрес: ')

def contact_copy():
    show_info()
    contact_num = input('Введите номер строки для копирования: ')
    index_contact = int(contact_num) - 1
    with open('phonebook_copy.txt', 'a', encoding='UTF-8') as file:
        file.write(show_info()[index_contact] + '\n\n')
        print(f'Контакт под номером {contact_num} успешно скопирован')

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

def add_contact(contact):
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)


def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        #print(file.read().rstrip())
        for contact in enumerate(contacts_list,1):
            print(*contact)
    return contacts_list

def search_contact():
    print(
    'Возможные варианты поиска:\n'
    '1. По фамилии\n'
    '2. По имени\n'
    '3. По отчеству\n'
    '4. По номеру телефона\n'
    '5. По адресу\n'
    )
    var_search = input('Выберите вариант поиска: ')

    while var_search not in ('1', '2', '3', '4', '5'):
        print('Некорректные данные, нужно ввести число комманды')
        var_search = input('Введите вариант поиска: ')

    index_var = int(var_search) - 1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        # print(contacts_list)

        for contact_str in contacts_list:
            contact_lst = contact_str.replace('\n', ' ').split()
            if search in contact_lst[index_var]:
                print(contact_str)

def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass
        command = '-1'

    while command != '5':
        print('Возможные варианты взаимодействия:\n'
        '1. Добавить контакт\n'
        '2. Вывести на экран\n'
        '3. Поиск контакта\n'
        '4. Копировать контакт\n'
        '5. Выход из программы')

        command = input('Введите номер действия: ')

        while command not in ('1', '2', '3', '4', '5'):
            print('Некорректные данные, нужно ввести число комманды')
            command = input('Введите номер действия: ')

        match command:
            case '1':
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                contact_copy()
            case '5':
                print('Всего хорошего!')

interface()