# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


my_file = open("task1.txt", "w")

while True:
    line = input('Введите строку: ')
    my_file.writelines(line + '\n')

    if not line:
        break

my_file.close()
