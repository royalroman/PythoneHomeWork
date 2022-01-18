# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from statistics import mean


with open("task3.txt") as workers:
    salaries = []
    for worker in workers:
        last_name, salary = worker.split()
        salary = float(salary)
        if salary < 20000:
            print(last_name, salary)
        salaries.append(salary)
    print('Средняя величина дохода сотрудников:', (mean(salaries)))
