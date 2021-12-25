# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def num_division():
    """"Функция деления чисел"""
    while True:
        try:
            num1 = float(input('Введите делимое число: '))
            num2 = float(input('Введите делитель: '))
            result = num1 / num2
        except ZeroDivisionError:
            print('Деление на ноль!')
        except ValueError:
            print('Это не число!')
        else:
            print(f'Результат:', result)


num_division()
