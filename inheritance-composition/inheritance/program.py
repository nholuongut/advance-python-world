import hr
import employees
import productivity

if __name__ == "__main__":

    manager = employees.Manager("1", "Mary Poppins", 3000)
    secretary = employees.Secretary("2", "John Smith", 1500)
    sales_guy = employees.SalesPerson("3", "Kevin Bacon", 1000, 250)
    factory_worker = employees.FactoryWorker("4", "Jane Doe", 40, 15)
    print(employees.TemperarySecretary.__mro__)
    temperary_secretary = employees.TemperarySecretary("5", "Himasha", 40, 9)

    employee_base = [
        manager,
        secretary,
        sales_guy,
        factory_worker,
    ]

    productivity_system = productivity.ProductivitySyetem()
    productivity_system.track(employees=employee_base, hours=40)

    payroll_system = hr.PayrollSystem()
    payroll_system.calculate_payroll(employee_base)
