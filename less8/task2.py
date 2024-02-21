class NotDivideToZero(Exception):
    def __init__(self):
        self.txt = "Нельзя делить на 0!"


try:
    dividend = int(input("Введите делимое: "))
    divider = int(input("Введите делитель: "))
    if divider == 0:
        raise NotDivideToZero()
except NotDivideToZero as err:
    print(err.txt)
else:
    print(f"Результат: {dividend / divider}")
