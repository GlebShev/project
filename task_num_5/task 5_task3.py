with open('task_3.txt') as file:
    lines = file.readlines()
salaries = []

for i in lines:
    surname, salary = i.split("-")
    salaries.append(int(salary))
    if int(salary) < 20000:
        print(f"Сотрудник {surname} имеет оклад {salary}")
print(f"Средняя зарплата: {sum(salaries) / len(salaries)}")