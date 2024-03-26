from Notes import *
def interface():
    lstcommand = ["add", "show all", "search note", "delete", "change note"]
    print("Доступные команды.\n1. add \n2. show all\n3. search note\n4. delete\n5. change note")
    command = input("Введи команду: ").lower()
    flag = False
    while(flag != True):
        if command not in lstcommand:
            print("Введена не верная команда")
            command = input("Введи команду: ").lower()
        else: flag = True
    
    match command:
            case 'add':
                add_notes(create_note())
            case "show all":
                show_all()
            case "search note":
                search_note()
            case "delete":
                deletedNote()
            case "change note":
                changeNote()
