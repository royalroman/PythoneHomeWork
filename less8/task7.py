class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b}'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a}'

    def __str__(self):
        return f'z = {self.a} + {self.b}'


z_1 = ComplexNumber(5, -3)
z_2 = ComplexNumber(2, 4)
print(z_1 + z_2)
print(z_1 * z_2)
