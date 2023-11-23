import unittest
from class_exercsie_1123 import Employee

class TestEmployee(unittest.TestCase):

    # 設置方法,創建一些示例員工對象
    def setUp(self):
        self.emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")  
        self.emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
        self.emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
        self.emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

    # 測試薪資字段的值 
    def test_salary(self):
        self.assertEqual(self.emp1.salary, 50000)  
        self.assertEqual(self.emp2.salary, 45000)

    # 測試部門字段的值
    def test_dept(self):
        self.assertEqual(self.emp3.department, "SALES")
        self.assertEqual(self.emp4.department, "OPERATIONS")

    # 測試計算薪資的方法邏輯 
    def test_calculate_salary(self):
        self.assertEqual(self.emp4.calculate_emp_salary(60), 58000)

if __name__ == '__main__':
    unittest.main()


    