from pathlib import Path

# data = ['Alex Korp,3000', 'Nikita Borisenko,2000', 'Sitarama Raju,1000']
# with open('Work/employee_data.txt', 'w', encoding='utf-8') as file:
# for line in data:
# file.write(f'{line}\n')

path = Path('Work/employee_data.txt')


def total_salary(path):
    try:
        salaries = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    continue
                try:
                    total = sum(salaries)
                    average = float(total / len(salaries))
                    return total, average
                except ZeroDivisionError:
                    return 0.0, 0.0

    except Exception as e:
        print(f'{e} with file')


total_salary(path)
