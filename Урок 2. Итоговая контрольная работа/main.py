import json
import random

Pets = ['dog', 'cat', 'hamster', "кошка", "собака", "хомяк"]


def get_data() -> list:
    list_pets = []
    with open('Pets.txt', 'r') as filePets:
        data = filePets.readlines()
        for i in data:
            list_pets.append(json.loads(i))
    return list_pets

def write_data(data: list):
    with open('Pets.txt', 'w') as filePets:
        for i in data:
            filePets.write(json.dumps(i, ensure_ascii=False) + '\n')


def add_animals(name: str, birthday: str, typePet: str, commands: list):
    animal = {"id": random.randrange(1, 1000), "Name": name, "Birthday": birthday, "TypePet": typePet, "Commands": commands}
    if typePet.lower() in Pets:
        with open('Pets.txt', 'a', encoding='utf-8') as filePets:
            filePets.write(json.dumps(animal, ensure_ascii=False) + '\n')
    else:
        with open('Animal.txt', 'a', encoding='utf-8') as fileAnimals:
            fileAnimals.write(json.dumps(animal, ensure_ascii=False) + '\n')


def get_commands_animal(name: str, typePet: str):
    if typePet.lower() in Pets:
        data = get_data()
        for pet in data:
            animal = pet
            if animal['Name'] == name.lower():
                print(f'Питомец {name} умеет:', ', '.join(animal['Commands']))


def learning_new_command(name:str, typePet:str):
    pets_list = []
    if typePet.lower() in Pets:
        data = get_data()
        for pet in data:
            animal = pet
            if animal['Name'] == name.lower():
                pets_list.append(animal)
        if len(pets_list) > 0:
            print('Нашли несколько питомцев с указанным именем.')
            for n, pet in enumerate(pets_list):
                print(n+1, f'Питомец {name} умеет: ', ', '.join(pet['Commands']))
            num_pet = int(input('Укажите номер питомца, которого хотите обучить новой команде')) - 1
            command = input('Введите команду, которой хотите обучить питомца')
            id_pet = pets_list[num_pet]["id"]
            selected_pet = pets_list[num_pet]["Commands"]
            selected_pet.append(command)
            for i in data:
                if i['id'] == id_pet:
                    write_data(data)
            print(f'Новая команда "{command}" изучена. Поздравляем!!!')


# add_animals('tom', '20.11.1996', 'cat', ['sit', 'give hand'])
# add_animals('adi', '20.11.1996', 'собака', ['sit', 'give hand'])
# add_animals('borya', '20.11.1996', 'horse', ['sit', 'give hand'])
learning_new_command('adi', 'собака')
# get_commands_animal('adi', 'собака')
# get_data()