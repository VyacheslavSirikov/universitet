# coding=utf-8
listcontact = {}

t = 1


def getname():
    a = input().title().strip()
    return a


def trans_name(listcontact, name, num):
    if name in listcontact:
        listcontact[name] = num
        print("\n Контак изменён\n")
    else:
        print("Контак не существует")
        return trans_name()


def delete_contact(listcontact, name):
    if name in listcontact:
        listcontact.pop(name)
        print("\nКонтакт удалён\n")
    else:
        print("Контак не существует")


def get_num():
    num = input("Введите номер телефона: ")
    num = num.replace(" ", "").replace("-", "")

    if num[0] == "9" and len(num) == 10:
        num = "+7" + num[1:]
        return num

    if num[0] == "8" and len(num) == 11:
        num = "+7" + num
        return num

    if num[0] == "7" and len(num) == 11:
        num = "+" + num
        return num

    if num[:2] == "+7" and len(num) == 12:
        return num

    else:
        print("Номер введён не коректно\n")
        return get_num()


def get_contact(listcontact, name, num):
    listcontact[name] = num
    print ("Контакт добавлен")
    return listcontact


def show_contact(listcontact):
    print("Список контактов: ")
    for i in listcontact:
        print(i, listcontact[i])


def menu():
    while True:
        print("Выберите действие: \n 1.Добавить контакт \n 2.Показать контакты \n 3.Удаление контакта \n 4.Изменить номер \n 5.Выход")

        p = int(input())

        if p == 1:
            get_contact(listcontact, getname(), get_num())

        if p == 2:
            show_contact(listcontact)

        if p == 3:
            delete_contact(listcontact, getname())

        if p == 4:
            trans_name(listcontact, getname(), get_num())

        if p == 5:
            break


menu()
