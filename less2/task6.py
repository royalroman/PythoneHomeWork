# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

from pprint import pprint


items = int(input('Введите ассортимент товаров: '))
item = 0
my_dict = {}
my_list = []
my_analys = {}


while item + 1 <= items:
    my_dict = dict({'Название товара': input('Введите название товара: '),
                    'Цена товара': int(input('Введите цену товара: ')),
                    'Количество едениц': int(input('Введите количество едениц товара: ')),
                    'Единица измерения': input('Введите еденицу измерения: ')})
    my_list.append((item + 1, my_dict))
    item += 1


    for key, value in my_dict.items():
        if key in my_analys:
            my_analys[key].append(value)
        else:
            my_analys[key] = [value]


pprint(my_list, sort_dicts=False)
pprint(my_analys, sort_dicts=False)