class Employee:
    # 創建Employee實例並初始化屬性
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):  
        self.name = emp_name  
        self.id = emp_id 
        self.salary = emp_salary
        self.department = emp_department
            
    # 計算薪資方法 
    def calculate_emp_salary(self, hours_worked):
        # 如果工時大於50
        if hours_worked > 50:  
            # 計算加班時間
            overtime = hours_worked - 50
            # 更具工資計算加班費
            overtime_pay = (overtime * (self.salary / 50)) 
            # 工資 + 加班費
            return self.salary + overtime_pay 
        else:
            # 如果不加班直接返回工資
            return self.salary
        
    # 分配新部門       
    def assign_department(self, new_department):
        self.department = new_department
        
    # 打印員工詳情
    def print_employee_details(self):
        print("Name: "+str(self.name))  
        print("ID: "+str(self.id))
        print("Salary: "+str(self.salary))
        print("Department: "+str(self.department))

emp1 = Employee("John Adams", "E7876", 50000, "Accounting") 
emp2 = Employee("Mary Jones", "E7499", 45000, "Research")
            
emp1.calculate_emp_salary(90)
emp1.assign_department("Sales") 
emp1.print_employee_details()

