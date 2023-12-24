# Phonebook

Фаил uui.py

from logger import input_data, print_data

def interface():
    print("Вы попали на специальный бот справочник от GeekBrains! \n 1 - запись данных \n 2 - вывод данных")
    command = int(input('Введите число:  '))
  
    while command != 1 and command != 2:          # Защита от неправильного ввода/ Если команда не равнв й и не равна 2, то
        print('Неправильный ввод')
        command = int(input('Введите число:  '))  # Просим снова ввести команду 1 или 2
        
    if command == 1:             # Если команда 1
        input_data()             # то вызываем функцию input_data(), для которой создаем новый файл logger.ry
    elif command == 2:           # Если команда 1
        print_data()             # то выводим функцию print_data(), для которой создаем новый файл logger.ry
                                 # В данном случае эти 2 функции будут вызывать ошибку, для чего мы их импортируем
                                 # и вставляем в верхней части  from logger import input_data, print_data, ошибка пропадает.
interface()

#_________________________________________________________________________________________________________________________________

фаил logger.py

from data_cgreate import name_data, surname_data, phone_data, address_data

def input_data():                 # сюда мы вводим новые функции.
    name = name_data()            # данные имени
    surname = surname_data()      # данные фамилии
    phone = phone_data()          # данные телефона
    address = address_data()      # данные адреса
                                  #  Эти функции показывают ошибку, для чего нужно создать новый файл с этими данными.
                                  #  и назовем его data_cgreate.py что переводится как "создание данных". В этом файле создаем функции
                                  #  name_data, surname_data, phone_data, address_data и импортируем их сюда (в верхнюю часть)
    
    var = int(input(f"В каком формате записать данные\n\n"
    f" 1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f" 2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выбери вариант: "))
 
    while var != 1 and var != 2:        # var - вариант, защита от не правильного ввода, данную функцию можно взять готовую,
                                        #  меняем только переменную c command на var
        print("Не правильный ввод")
        var = int(input("Введите число "))
   
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")
#
def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(' '.join(data_first[j:i + 1]))
                j = i
        print(' '.join(data_first_list))

    print("Вывожу данные из 2 файла: \n")
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

#_____________________________________________________________________________________________________________________________________

Фаил data_cgreate.py

def name_data():
    name = input('Введите Ваше имя: ')
    print('Очень красивое имя!')
    return name


def surname_data():
    surname = input('Введите Вашу фамилию: ')
    return surname
#\

def phone_data():
    phone = input('Введите Ваш номер телефона: ')
    return phone

def address_data():
    address = input('Введите Ваш адрес: ')
    return address

#_____________________________________________________________________________________________________________________________________

фаил main.py

from uui import interface

if __name__ == '__main__':
    interface()























































