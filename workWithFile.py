def add_contact(data_list, name_file):
    with open(name_file, "a", encoding='utf-8') as data:
        for el in data_list:
            data.write(f"{el} ")
        data.write("\n")

def show_file(name_file):
    with open(name_file, "r", encoding='utf-8') as data:
        print(data.read())

def search_data(person, name_file):
    with open(name_file, "r", encoding='utf-8') as data:
        for el in data:
            if person in el.lower().split():
                return el
                
        else:
            return ""

def delet_data(person, name_file):
    data_line = search_data(person, name_file)
    if data_line != "":
        with open(name_file, "r", encoding='utf-8') as data:
            data_file = data.readlines()
        with open(name_file, "w", encoding='utf-8') as data:
            for el in data_file:
                if el != data_line:
                    data.write(el)
    else:
        print("Такого нету!")

def data_changes(person, name_file):
    data_line = search_data(person, name_file)
    if data_line != "":
        with open(name_file, "r", encoding='utf-8') as data:
            data_file = data.readlines()
        with open(name_file, "w", encoding='utf-8') as data:
            for el in data_file:
                if el != data_line:
                    data.write(el)
                else:
                    person = input("Введите Фамилия, имя, отчество, "
                                   "номер телефона: ")    
                    data.write(f"{person} \n")
    else:
        print("Такого нету!")