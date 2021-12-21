# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым
# результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

name = input('Здравствуйте, как я могу к вам обращаться? ')
proceeds = int(input(f'{name}, сколько денег в этом месяце ваша фирма заработала? '))
cost = int(input(f'{name}, а сколько денег в этом месяце ваша фирма потратила? '))

if cost > proceeds:
    print(f'{name}, К сожалению вы работаете в убыток ')
elif cost < proceeds:
    print(f'{name}, Мои поздравления, ваша фирма приносит прибыль')
    print('Рентабельность в этом месяце составила', int((proceeds - cost) / proceeds * 100), '%')
    num_work = int(input('Какая численность сотрудников в вашей фирме? '))
    print('Каждый сотрудник вашей фирмы в среднем приносит - ', int((proceeds - cost) / num_work))
else:
    print('Ну у вас еще все впереди!)')