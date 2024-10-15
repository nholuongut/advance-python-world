from productivity import ProductivitySyetem
from payroll import PayrollSyetem
from employee_entity import Employee
from contacts import Address, AddressBook


class EmployeeDatabase:
    def __init__(self) -> None:
        self._employees = [
            {"id": 1, "name": "Mary Poppins", "role": "manager"},
            {"id": 2, "name": "John Smith", "role": "secretary"},
            {"id": 3, "name": "Kevin Bacon", "role": "sales"},
            {"id": 4, "name": "Jane Doe", "role": "factory"},
            {"id": 5, "name": "Robin Williams", "role": "secretary"},
        ]

        # initialize systems
        self.productivity_system = ProductivitySyetem()
        self.payroll_system = PayrollSyetem()
        self.contact_system = AddressBook()

    @property
    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id: int, name: str, role: str):
        # extract the address
        address = self.contact_system.get_employee_address(employee_id=id)
        responsibility = self.productivity_system.get_role(role_id=role)
        policy = self.payroll_system.get_policy(employee_id=id)
        return Employee(
            id=id,
            name=name,
            address=address,
            role=responsibility,
            payrole=policy,
        )
