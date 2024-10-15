class ProductivitySyetem:
    def track(self, employees, hours):
        print("Tracking the Employee Productivity\n")
        print("=================================\n")
        for employee in employees:
            employee.work(hours)
        print(" ")
