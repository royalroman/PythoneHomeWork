# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def collection_data(name, surname, year, city, email, telephone):
    """Функция собирает данные о пользователе"""
    return ' '.join([name, surname, year, city, email, telephone])


result = collection_data(surname = 'Alexandrov', name = 'Stas', year = '1988', city = 'Konotop',
                         email = 'qwerty@gmail.com', telephone = '555 55 55')
print(result)
