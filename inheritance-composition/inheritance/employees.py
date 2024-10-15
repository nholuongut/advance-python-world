from hr import SalaryEmployee, ComnissionEmployee, HourlyEmployee

# define each role


class Manager(SalaryEmployee):
    def work(self, hours: float):
        print(f"{self.name} screems and yells for {hours}")


class Secretary(SalaryEmployee):
    def work(self, hours: float):
        print(f"{self.name} expends {hours} hours doing office paperwork.")


class SalesPerson(ComnissionEmployee):
    def work(self, hours: float):
        print(f"{self.name} expends {hours} hours on the phone.")


class FactoryWorker(HourlyEmployee):
    def work(self, hours: float):
        print(f"{self.name} manufactures gadgets for {hours} hours.")


class TemperarySecretary(Secretary, HourlyEmployee):
    # according to the method resolution order (MRO) for initialize classes python follows special flow
    def __init__(
        self, id: str, name: str, hours_worked: float, hourly_rate: float
    ) -> None:
        HourlyEmployee.__init__(self, id, name, hours_worked, hourly_rate)

    # if we have not overwritten the payment calculate method bydefault python uses SalaryEmployee paycalculator
    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)
