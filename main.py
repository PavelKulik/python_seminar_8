from interface import *
from workWithFile import *
import os


os.system('cls' if os.name == 'nt' else 'clear')
while True:
    main()
    command = input("Введите команду: ")
    if command == "1":
        person = input("Введите Фамилия, имя, отчество, номер телефона: ").split()
        add_contact(person, "test.txt")
    elif command == "2":
        show_file('test.txt')
    elif command == "3":
        element = input("Введите элемент для поиска: ").lower()
        data = search_data(element, "test.txt")
        if data == "":
            print("Такого элемента нету!")
        else:
            print(data)
    elif command == "4":
        element = input("Введите элемент для удаления: ").lower()
        delet_data(element, "test.txt")
    elif command == "5":
        element = input("Введите элемент для изменения: ").lower()
        data_changes(element, "test.txt")
    elif command == "6":
        break
    else:
        print("Ввод некорректен")




'''add_contact(["Pavel", "Kulik", "Leonidovich", "+375298181356"], "test.txt")
show_file('test.txt')
print(search_data("pavel", "test.txt"))
delet_data("pavel2", "test.txt")
data_changes("pavel3", "test.txt")
show_file('test.txt')'''