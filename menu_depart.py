"""
Модуль csv предоставляет функциональность для работы с файлами CSV.
"""
import csv


def depart_teams():
    """
        Функция для отображения департаментов и всех команд, входящих в них.

        Читает данные из файла 'Corp_Summary.csv' и
        выводит информацию о департаментах и связанных с ними командах.
    """
    depart_and_team = {}

    with open('Corp_Summary.csv', newline = '', encoding = 'utf-8') as corp:
        reader = csv.DictReader(corp, delimiter = ';')
        for row in reader:
            if not depart_and_team.get(row['Департамент']):
                depart_and_team[row['Департамент']] = []

            if row['Отдел'] not in depart_and_team[row['Департамент']]:
                depart_and_team[row['Департамент']].append(row['Отдел'])

    for key, value in depart_and_team.items():
        print(f"{key}: {', '.join(value)}")

def consolidated_report():
    """
        Функция для создания сводного отчёта по департаментам.

        Читает данные из файла 'Corp_Summary.csv'
        и выводит сводный отчёт о численности, вилке зарплат и средней зарплате
        в каждом департаменте.
    """
    depart_fork = {}

    with open('Corp_Summary.csv', newline='', encoding='utf-8') as corp:
        reader = csv.DictReader(corp, delimiter=';')
        for row in reader:
            department = row['Департамент']
            salary = int(row['Оклад'])

            if department not in depart_fork:
                depart_fork[department] = {
                    'count': 0,
                    'salaries': []
                }

            depart_fork[department]['count'] += 1
            depart_fork[department]['salaries'].append(salary)

    for key, values in depart_fork.items():
        count = values['count']
        salaries = values['salaries']
        min_salary = min(salaries)
        max_salary = max(salaries)
        average_salary = sum(salaries) / len(salaries)

        print(
            f"Департамент {key}:\n"
            f"\tЧисленность: {count}\n"
            f"\tВилка: {min_salary} - {max_salary}\n"
            f"\tСредняя зарплата: {average_salary:.2f}"
        )


def save_report():
    """
    Функция для сохранения сводного отчёта в файл 'sw_data_new.csv'.
    Читает данные из файла 'Corp_Summary.csv', создаёт сводный отчёт
    и сохраняет его в виде CSV-файла 'sw_data_new.csv'.
    """
    depart_fork = {}

    with open('Corp_Summary.csv', newline='', encoding='utf-8') as corp:
        reader = csv.DictReader(corp, delimiter=';')
        for row in reader:
            department = row['Департамент']
            salary = int(row['Оклад'])

            if department not in depart_fork:
                depart_fork[department] = {
                    'count': 0,
                    'salaries': []
                }

            depart_fork[department]['count'] += 1
            depart_fork[department]['salaries'].append(salary)

    with open('sw_data_new.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

        # Записываем заголовок CSV
        writer.writerow(["Департамент", "Численность", "Вилка", "Средняя зарплата"])

        for key, values in depart_fork.items():
            count = values['count']
            salaries = values['salaries']
            min_salary = min(salaries)
            max_salary = max(salaries)
            average_salary = sum(salaries) / len(salaries)
            writer.writerow([key, count, f"{min_salary}-{max_salary}", average_salary])

def menu():
    """
        Функция для отображения меню выбора функций.

        Выводит меню с выбором функций и выполняет выбранную функцию.
    """
    print(
        "Здравствуйте,выберите функцию меню:\n" 
        "1: Департамент и все команды, которые входят в него\n"
        "2: Cводный отчёт по департаментам\n"
        "3: Сохранить сводный отчёт"
    )
    option = str(input('Выберите: '))
    options = {'1': depart_teams, '2': consolidated_report, '3': save_report}
    while option not in options:
        print(
            f'Выберите:\n'
            f'{options["1"]}: Департамент и все команды, которые входят в него\n'
            f'{options["2"]}: Сводный отчёт по департаментам\n'
            f'{options["3"]}: Сохранить сводный отчёт'
        )
        option = str(input())

    return options[option]()

if __name__ == '__main__':
    menu()
