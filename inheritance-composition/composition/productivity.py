# define each roles
from employee_entity import Employee
from typing import Iterable


class ManagerRole:
    def perform_duties(self, hours: float):
        return f"screams and yells for {hours}"


class SecreteryRole:
    def perform_duties(self, hours: float):
        return f"does paperwork for {hours}"


class SalesRole:
    def perform_duties(self, hours: float):
        return f"expends {hours} hours on the phone"


class FactoryRole:
    def perform_duties(self, hours: float):
        return f"manufactures gadgets for {hours} hours."


class ProductivitySyetem:
    def __init__(self) -> None:
        self._roles = {
            "manager": ManagerRole(),
            "secretary": SecreteryRole(),
            "sales": SalesRole(),
            "factory": FactoryRole(),
        }

    def get_role(self, role_id: str):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError(role_id)

        else:
            return role_type

    def track(self, employees: Iterable[Employee], hours: int):
        print("Tracking Employee Productivity ...\n")
        for employee in employees:
            employee.work(hours)
            print("==========================")
