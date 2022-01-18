# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда); опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
# методы и покажите результат.


class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Машина: {self.name}, Цвет: {self.color}, Машина полицейская - {self.is_police}')

    def go(self):
        print(f'{self.name}: Машина поехала')

    def stop(self):
        print(f'{self.name}: Машина остановилась')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}')

    def show_speed(self):
        print(f'{self.name}: Скорость автомобиля - {self.speed}')


class WorkCar(Car):

    def show_speed(self):
        return print(f'{self.name}: Скорость автомобиля - {self.speed} - Превышение скорости!'
            if self.speed > 40 else f'{self.name}: Скорость автомобиля - {self.speed}')


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('ДПС', 'Синий', 50)
police_car.go()
police_car.show_speed()
police_car.stop()

work_car = WorkCar('Газель', 'Белая', 80)
work_car.go()
work_car.turn(1)
work_car.show_speed()
