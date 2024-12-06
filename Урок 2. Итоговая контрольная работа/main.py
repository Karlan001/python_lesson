import json
import random

Pets = ["Домашний", "Домашнее", "Домашняя"]


def get_data(type_pet: str) -> list:
    list_pets = []
    if type_pet in Pets:
        with open('Pets.txt', 'r') as filePets:
            data = filePets.readlines()
            for i in data:
                list_pets.append(json.loads(i))
        return list_pets
    else:
        with open('Animal.txt', 'r') as filePets:
            data = filePets.readlines()
            for i in data:
                list_pets.append(json.loads(i))
        return list_pets


def write_data(data: list, type_pet: str):
    if type_pet in Pets:
        with open('Pets.txt', 'w') as filePets:
            for i in data:
                filePets.write(json.dumps(i, ensure_ascii=False) + '\n')
    else:
        with open('Animal.txt', 'w') as filePets:
            for i in data:
                filePets.write(json.dumps(i, ensure_ascii=False) + '\n')


def add_animals(name: str, birthday: str, type_pet: str):
    animal = {"id": random.randrange(1, 1000), "Name": name, "Birthday": birthday, "TypePet": type_pet,
              "Commands": list()}
    if type_pet.lower() in Pets:
        with open('Pets.txt', 'a', encoding='utf-8') as filePets:
            filePets.write(json.dumps(animal, ensure_ascii=False) + '\n')
    else:
        with open('Animal.txt', 'a', encoding='utf-8') as fileAnimals:
            fileAnimals.write(json.dumps(animal, ensure_ascii=False) + '\n')
    print(f'Добавлен питомец {name}')
    print()


def get_commands_animal(name: str, type_pet: str):
    data = get_data(type_pet)
    count = 0
    for pet in data:
        animal = pet
        animal_name = animal['Name']
        if animal_name.lower() == name.lower():
            count += 1
            print(f'{count} Питомец {name} умеет:', ', '.join(animal['Commands']))
    print()


def learning_new_command(name: str, type_pet: str):
    pets_list = []
    data = get_data(type_pet)
    for pet in data:
        animal = pet
        animal_name = animal['Name']
        if animal_name.lower() == name.lower():
            pets_list.append(animal)
    if len(pets_list) > 1:
        print('Нашли несколько питомцев с указанным именем.')
        for n, pet in enumerate(pets_list):
            print(n + 1, f'Питомец {name} умеет: ', ', '.join(pet['Commands']))
        num_pet = int(input('Укажите номер питомца, которого хотите обучить новой команде: ')) - 1
        command = input('Введите команду, которой хотите обучить питомца: ')
        id_pet = pets_list[num_pet]["id"]
        selected_pet = pets_list[num_pet]["Commands"]
        selected_pet.append(command)
        for i in data:
            if i['id'] == id_pet:
                write_data(data, type_pet)
        print(f'Новая команда "{command}" изучена питомцем {name}. Поздравляем!!!')
        print()
    else:
        for n, pet in enumerate(pets_list):
            print(n + 1, f'Питомец {name} умеет: ', ', '.join(pet['Commands']))
        command = input('Введите команду, которой хотите обучить питомца: ')
        id_pet = pets_list[0]["id"]
        selected_pet = pets_list[0]["Commands"]
        selected_pet.append(command)
        for i in data:
            if i['id'] == id_pet:
                write_data(data, type_pet)
        print(f'Новая команда "{command}" изучена питомцем {name}. Поздравляем!!!')
        print()


def show_quantity_animals():
    pets = get_data('dog')
    animals = get_data('as')
    print(f'Количество вьючных и домашних питомцев - {len(pets) + len(animals)}')
    print()


def main():
    flag = True
    while flag:
        action = int(input('Что необходимо сделать? Введите номер действия: \n'
                           '1. Посмотреть список команд питомцев.\n2. Добавить нового питомца.\n'
                           '3. Обучить новой команде.\n'
                           '4. Узнать количество питомцев\n5. Выход\n'))
        match action:
            case 1:
                try:
                    name, type_pet = input(
                        'Введите имя питомца и его тип (домашнее, вьючное) через пробел: ').split()
                    get_commands_animal(name, type_pet)
                except ValueError:
                    print('Введены не все необходимые данные')
                    main()
            case 2:
                try:
                    name, birthday, type_pet = input(
                        'Введите имя, дату рождения, тип питомца (вьючное, домашнее) '
                        'через пробел: ').split()
                    add_animals(name, birthday, type_pet)
                except ValueError:
                    print('Введены не все необходимые данные')
                    main()
            case 3:
                try:
                    name, type_pet = input(
                        'Введите имя питомца и его тип (вьючное, домашнее) через пробел: ').split()
                    learning_new_command(name, type_pet)
                except ValueError:
                    print('Введены не все необходимые данные')
                    main()
            case 4:
                show_quantity_animals()
            case 5:
                flag = False


if __name__ == '__main__':
    main()
