from abc import ABC, abstractmethod
from typing import Iterable


# define employee class
class Employee(ABC):
    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self) -> float: ...


# define employee types
class SalaryEmployee(Employee):
    def __init__(self, id: str, name: str, weekly_salary: float) -> None:
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(
        self, id: str, name: str, hours_worked: float, hourly_rate: float
    ) -> None:
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hourly_rate * self.hours_worked


class ComnissionEmployee(SalaryEmployee):
    def __init__(
        self, id: str, name: str, weekly_salary: float, commission: float
    ) -> None:
        super().__init__(id, name, weekly_salary)
        self.weekly_salary = weekly_salary
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class PayrollSystem:
    def calculate_payroll(self, employees: Iterable[Employee]):
        print("Calculating Payroll ...")

        for employee in employees:
            print(f"Payroll for : {employee.id} - {employee.name}")
            print("+++++++++++++++++++++")
            print(f"Employee Payroll : {employee.calculate_payroll()}")
