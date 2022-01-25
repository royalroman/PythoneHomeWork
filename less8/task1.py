class Date:
    date = None
    day = None
    month = None
    year = None

    def __init__(self, date):
        self.__class__.date = date

    def __str__(self):
        return self.date

    @classmethod
    def to_int(cls):
        date = [int(s) for s in cls.date.split('-')]
        cls.day = date[0]
        cls.month = date[1]
        cls.year = date[2]
        print(f'Текущая дата {cls.day} день, {cls.month} месяц, {cls.year} год')

    @staticmethod
    def validate(d):
        if d.day > 31 or d.day < 1:
            print(f'{d.day} не является днем!')
        if d.month > 12 or d.month < 1:
            print(f'{d.month} не является месяцем!')
        if d.year < 0:
            print(f'{d.year} не является годом!')
        raise Exception("Не верные данные!")


d = Date("166-15-2022")
d.to_int()
Date.validate(d)
