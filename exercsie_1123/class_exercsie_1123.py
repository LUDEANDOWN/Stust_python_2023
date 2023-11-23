class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.name = emp_name 
        self.id = emp_id
        self.salary = emp_salary
        self.department = emp_department
        
    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_pay = (overtime * (self.salary / 50))
            return self.salary + overtime_pay
        else:
            return self.salary
        
    def assign_department(self, new_dept):
        self.department = new_dept
        
    def print_employee_details(self):
        print(f"Name: {self.name}") 
        print(f"ID: {self.id}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

emp1 = Employee("John Adams", "E7876", 50000, "Accounting")
emp2 = Employee("Mary Jones", "E7499", 45000, "Research") 

emp1.calculate_emp_salary(55) 
emp1.assign_department("Sales")
emp1.print_employee_details()

