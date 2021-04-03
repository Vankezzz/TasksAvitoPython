from dataclasses import dataclass
from typing import List


@dataclass
class SampleCSV:
    initials: str
    position: str
    departmentHierarchy: str
    quarterlyEstimate: float
    salary: int


@dataclass
class DepartmentReport:
    department: str
    number: int
    minSalary: int
    maxSalary: int
    averageSalary: int


# maybe I will do it
# @dataclass
# class Person:
#     initials: str
#     salary: int
#
#
# @dataclass
# class Department:
#     department: str
#     people: List[Person]


def read_to_end(path: str, separator: str = ";") -> List[SampleCSV]:
    """ The function reads file.csv in the path and divides data by separator and row
    after that returns data in List[SampleCSV] """
    samples = []
    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            data = line.split(separator)
            sample = SampleCSV(initials=data[0], position=data[1], departmentHierarchy=data[2],
                               quarterlyEstimate=float(data[3]), salary=int(data[4]))
            samples.append(sample)
    return samples


def save_report_by_department(data_csv: List[SampleCSV], name: str):
    """ The function saves the report by departments from data_csv in path with name"""
    report = write_report_by_department(data_csv)
    report_str = "\n".join(
        ";".join((x.department, str(x.number), str(x.minSalary), str(x.maxSalary), str(x.averageSalary))) for x in
        report)
    f = open(name + ".csv", 'w')
    f.write(report_str)
    f.close()


def write_all_department(data_csv: List[SampleCSV]) -> List[str]:
    """ The function returns all departments from data_csv as List[str]"""
    departments = []
    for sample in data_csv:
        if sample.departmentHierarchy not in departments:
            departments.append(sample.departmentHierarchy)
    return departments


def write_report_by_department(data_csv: List[SampleCSV]) -> List[DepartmentReport]:
    """ The function returns the report by departments from data_csv as List[DepartmentReport]"""
    departments = write_all_department(data_csv)
    report = []
    departments_salary = {}
    for i in departments:
        departments_salary[i] = []

    for sample in data_csv:
        if sample.departmentHierarchy in departments:
            departments_salary.get(sample.departmentHierarchy).append(sample.salary)
    for i in departments:
        salary_list = departments_salary.get(i)
        salary_list.sort()
        report.append(DepartmentReport(department=i,
                                       number=salary_list.__len__(),
                                       minSalary=salary_list[0],
                                       maxSalary=salary_list[-1],
                                       averageSalary=sum(salary_list) // len(salary_list)))

    return report
