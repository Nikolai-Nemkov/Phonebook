# Phonebook

from logger import input_data, print_data
#
#
def interface():
    print("Вы попали на специальный бот справочник от GeekBrains! \n 1 - запись данных \n 2 - вывод данных")
    command = int(input('Введите число:  '))
    #
    while command != 1 and command != 2:  # Защита от неправильного ввода/ Если команда не равнв й и не равна 2, то
        print('Неправильный ввод')
        command = int(input('Введите число:  '))  # Просим снова ввести команду 1 или 2

# interface()  # - вызов команды для проверки и отработки написанного кода, нажимаем кнопку принт
    # Вы попали на специальный бот справочник от GeekBrains!
    #  1 - запись данных
    #  2 - вывод данных
    # Введите число  5
    # Неправильный ввод

    if command == 1:  # Если команда 1
        input_data()  # то вызываем функцию input_data(), для которой создаем новый файл logger.ry
    elif command == 2:  # Если команда 1
        print_data()  # то выводим функцию print_data(), для которой создаем новый файл logger.ry
    # В данном случае эти 2 функции будут вызывать ошибку, для чего мы их импортируем
    # и вставляем в верхней части  from logger import input_data, print_data, ошибка пропадает.
interface()
