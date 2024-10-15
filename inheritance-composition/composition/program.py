from payroll import PayrollSyetem
from productivity import ProductivitySyetem
from hr_system import EmployeeDatabase


if __name__ == "__main__":

    productivity_system = ProductivitySyetem()
    payroll_system = PayrollSyetem()
    employee_database = EmployeeDatabase()

    employees = employee_database.employees
    productivity_system.track(employees, 40)
    payroll_system.calculate_payroll(employees)
