# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Меньше нуля!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        rows, nums = self.quantity // cells_in_row, self.quantity % cells_in_row
        return '\\n'.join(['*' * cells_in_row] * rows + (['*' * nums] if nums else []))


cells1 = Cell(12)
cells2 = Cell(15)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells1 * cells2)
print(cells2 / cells1)
print(cells1.make_order(5))
print(cells2.make_order(5))
