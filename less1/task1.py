# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.
a = 2
b = 7
c = 25
d = (a + b) * c

print(a, b, c, d)

a1 = int(input('Введите первое число: '))
b1 = int(input('Введите второе число: '))
c1 = input('Как ваз зовут? ')
d1 = input('В каком городе вы проживаете? ')

print('Сумма ваших чисел - ', a1 + b1)
print(f'Ваше имя {c1} и вы проживаете в городе {d1}')