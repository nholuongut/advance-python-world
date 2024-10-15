from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, id, name, address, role, payrole) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payrole = payrole

    def work(self, hours: float):
        duties = self.role.perform_duties(hours=hours)
        print(f"Employee : {self.id} - {self.name}")
        print(duties)
        # track the working hours
        self.payrole.track_work(hours)

    def calculate_check(self):
        return self.payrole.calculate_payroll()
