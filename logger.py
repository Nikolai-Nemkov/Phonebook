from data_cgreate import name_data, surname_data, phone_data, address_data


def input_data():  # сюда мы вводим новые функции.
    name = name_data()  # данные имени
    surname = surname_data()  # данные фамилии
    phone = phone_data()  # данные телефона
    address = address_data()  # данные адреса
    #     Эти функции показывают ошибку, для чего нужно создать новый файл с этими данными.
    #     и назовем его data_cgreate.py что переводится как "создание данных". В этом файле создаем функции
    #     name_data, surname_data, phone_data, address_data и импортируем их сюда (в верхнюю часть)
    #
    var = int(input(f"В каком формате записать данные\n\n"
    f" 1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f" 2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выбери вариант: "))
    #
    # input_data()    # - вызов команды для проверки и отработки написанного кода, нажимаем кнопку пуск
    #    Введите Ваше имя: sddv
    #     Введите Вашу фамилию: hrthf
    #     Введите Ваш номер телефона: rtjrt
    #     Введите Ваш адрес: rtjrtj
    #     В каком формате записать данные
    #
    #      1 Вариант:  в столбец
    #     sddv
    #     hrthf
    #     rtjrt
    #     rtjrtj
    #
    #      2 Вариант:   в строку
    #     sddv, hrthf,  rtjrt, # rtjrtj    в строку

    while var != 1 and var != 2:  # var - вариант, защита от не правильного ввода, данную функцию можно взять готовую,
                                    #     меняем только переменную c command на var
        print("Не правильный ввод")
        var = int(input("Введите число "))
    #
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
#
#
