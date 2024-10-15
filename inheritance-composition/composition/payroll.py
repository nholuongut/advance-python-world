from employee_entity import Employee
from typing import Iterable


# define employee paypolicies
class PayrollPolicy:
    def __init__(self) -> None:
        self.hours_worked = 0

    def track_work(self, hours: float):
        self.hours_worked += hours


class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary: float) -> None:
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):
    def __init__(self, hourly_rate: float) -> None:
        super().__init__()
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary: float, commission_per_sale: float) -> None:
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    @property
    def commission(self):
        sales = self.hours_worked / 5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        return self.commission + super().calculate_payroll()


class PayrollSyetem:
    def __init__(self) -> None:
        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9),
        }

    def get_policy(self, employee_id: int):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            raise ValueError(employee_id)

        return policy

    def calculate_payroll(self, employees: Iterable[Employee]):
        print("Calculating PayRoll")
        print("=============================")

        for employee in employees:
            print(f"Payroll for : {employee.id} - {employee.name}")
            print(f"Check Amount : {employee.calculate_check()}")

            if employee.address:
                print(f"Sent to :\n")
                print(employee.address)
