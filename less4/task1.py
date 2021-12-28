# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


def salary(worked_hours, pay_per_hour, bonus):
    """Функция расчета заработной платы"""
    return worked_hours * pay_per_hour + bonus


ivanov = salary(50, 20, 0)
karpov = salary(66, 15, 30)

print(f'{ivanov = }\n{karpov = }'.title())
