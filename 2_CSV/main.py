import sys

import CSV
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s - %(asctime)s')
greeting = "Привет, укажи путь до файла с разрешением .csv"
menuOptions = """
\nМеню действий:
1. Вывести все отделы
2. Вывести сводный отчёт по отделам
3. Сохранить сводный отчёт в CSV-файл
4. Выйти из программы\n"""

if __name__ == '__main__':
    print(greeting)
    path = input('\nУказанный путь:')
    try:
        samples = CSV.read_to_end(path)
        options = {
            '1': "\n".join(x for x in CSV.write_all_department(samples)),
            '2': "\n".join(
                ";".join((x.department, str(x.number), str(x.minSalary), str(x.maxSalary), str(x.averageSalary))) for x
                in
                CSV.write_report_by_department(samples)),
            '3': "Successful",
            '4': "GoodBye",
        }
        while True:
            option = ''
            print(menuOptions)
            while option not in options:
                option = input('\nВаш выбор:\n')
                if option == '3':
                    CSV.save_report_by_department(samples, "report")
                elif option == '4':
                    print(options[option])
                    sys.exit()
            print(options[option])
    except Exception as e:
        print(e)
