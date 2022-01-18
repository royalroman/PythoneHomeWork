#  Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationary:

    def __init__(self, title = 'отрисовку'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print(f'Ручка пишет {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Карандаш чертит {self.title}')


class Marker(Stationary):
    def draw(self):
        print(f'Маркер рисует {self.title}')


stat = Stationary()
stat.draw()

pen = Pen()
pencil = Pencil()
mark = Marker()

pen.draw()
pencil.draw()
mark.draw()
