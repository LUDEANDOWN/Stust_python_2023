class Employer:
    def __init__(self, name, seniority, hours_worked):#三個屬性,名子,年資,工作時數(當月)
        self.name = name
        self.seniority = seniority
        self.hours_worked = hours_worked

    def query_name(self):#查詢員工名稱副函式
        return f"員工名稱: {self.name}"

    def query_seniority(self):#查詢員工年資副函式
        return f"員工年資: {self.seniority} 年"

    def query_hours_worked(self):#查詢工作時數副函式
        return f"本月工作時數: {self.hours_worked} 小時"

    def calculate_monthly_salary(self, hourly_rate):#查詢月薪副函式
        return f"月薪: ${self.hours_worked * hourly_rate}"

    def increase_hours_worked(self, additional_hours):#增加的工作時數副函式
        self.hours_worked += additional_hours
        return f"工時增加 {additional_hours} 小時"

    def increase_seniority(self, additional_years):#增加的年資副函式
        self.seniority += additional_years
        return f"年資增加 {additional_years} 年"


class Drink:
    def __init__(self, name, ice_level, sweetness, price):#4個屬性,名子,冰量,甜度,價錢
        self.name = name#名子
        self.ice_level = ice_level#冰量
        self.sweetness = sweetness#甜度
        self.price = price  # 價錢

    def modify_name(self, new_name):#修改名稱副函式
        self.name = new_name
        return f"飲料名稱修改為: {self.name}"

    def adjust_sweetness(self, new_sweetness):#調整甜度副函式
        self.sweetness = new_sweetness
        return f"甜度調整為: {self.sweetness}"

    def adjust_price(self, new_price):#調整價錢副函式
        self.price = new_price
        return f"價格調整為: ${self.price}"


class ColdDrink(Drink):#ColdDrink繼承Drink類別
    def __init__(self, name, ice_level, sweetness, price):
        super().__init__(name, ice_level, sweetness, price)#繼承Drink
    def Ice_level(self, ice_level):#調整甜度副函式
        self.ice_level = ice_level
        return f"冰量調整為: {self.ice_level}"


class HotDrink(Drink):#HotDrink繼承Drink類別
    def __init__(self, name, sweetness, price):
        super().__init__(name, ice_level=None, sweetness=sweetness, price=price)#繼承Drink

# 創建員工1物件
employer1 = Employer(name="約翰", seniority=5, hours_worked=160)
# 呼叫員工1副函式
print(employer1.query_name())  # 查詢員工名稱
print(employer1.query_seniority())  # 查詢員工年資
print(employer1.query_hours_worked())  # 查詢工作時數
print(employer1.calculate_monthly_salary(hourly_rate=10))  # 查詢月薪
print(employer1.increase_hours_worked(10))  # 增加的工作時數
print(employer1.increase_seniority(6))  # 增加的年資
print("\n")

# 創建員工2物件
employer2 = Employer(name="大明", seniority=7, hours_worked=150)
# 呼叫員工2副函式
print(employer2.query_name())  # 查詢員工名稱
print(employer2.query_seniority())  # 查詢員工年資
print(employer2.query_hours_worked())  # 查詢工作時數
print(employer2.calculate_monthly_salary(hourly_rate=20))  # 查詢月薪
print(employer2.increase_hours_worked(5))  # 增加的工作時數
print(employer2.increase_seniority(8))  # 增加的年資
print("\n")

# 創建員工3物件
employer3 = Employer(name="中忠", seniority=6, hours_worked=170)
# 呼叫員工3副函式
print(employer3.query_name())  # 查詢員工名稱
print(employer3.query_seniority())  # 查詢員工年資
print(employer3.query_hours_worked())  # 查詢工作時數
print(employer3.calculate_monthly_salary(hourly_rate=10))  # 查詢月薪
print(employer3.increase_hours_worked(20))  # 增加的工作時數
print(employer3.increase_seniority(7))  # 增加的年資
print("\n")

# 創建冷飲1物件
cold_drink1 = ColdDrink(name="冰茶", ice_level="少冰", sweetness="半糖", price=2)
# 呼叫冷飲1副函式
print(cold_drink1.modify_name("冰檸檬茶"))  # 修改名稱
print(cold_drink1.Ice_level("全冰"))# 修改冰量
print(cold_drink1.adjust_sweetness("少糖"))  # 調整甜度
print(cold_drink1.adjust_price(3))  # 調整價錢
print("\n")

# 創建冷飲2物件
cold_drink2 = ColdDrink(name="冬瓜茶", ice_level="中冰", sweetness="少糖", price=1)
# 呼叫冷飲2副函式
print(cold_drink2.modify_name("綠豆沙"))  # 修改名稱
print(cold_drink2.Ice_level("全冰"))# 修改冰量
print(cold_drink2.adjust_sweetness("無糖"))  # 調整甜度
print(cold_drink2.adjust_price(4))  # 調整價錢
print("\n")

# 創建冷飲3物件
cold_drink3 = ColdDrink(name="啤酒", ice_level="多冰", sweetness="無糖", price=3)
# 呼叫冷飲3副函式
print(cold_drink3.modify_name("珍珠奶茶"))  # 修改名稱
print(cold_drink3.Ice_level("少冰"))# 修改冰量
print(cold_drink3.adjust_sweetness("全糖"))  # 調整甜度
print(cold_drink3.adjust_price(5))  # 調整價錢
print("\n")

# 創建熱飲1物件
hot_drink1 = HotDrink(name="熱咖啡", sweetness="半糖", price=3)
# 呼叫熱飲副函式
print(hot_drink1.modify_name("卡布奇諾"))  # 修改名稱
print(hot_drink1.adjust_sweetness("少糖"))  # 調整甜度
print(hot_drink1.adjust_price(4))  # 調整價錢
print("\n")

# 創建熱飲2物件
hot_drink2= HotDrink(name="白玉珍珠太妃鮮奶", sweetness="無糖", price=5)
# 呼叫熱飲副函式
print(hot_drink2.modify_name("芋芋三混圓"))  # 修改名稱
print(hot_drink2.adjust_sweetness("少糖"))  # 調整甜度
print(hot_drink2.adjust_price(6))  # 調整價錢
print("\n")

# 創建熱飲3物件
hot_drink3= HotDrink(name="碎銀普洱茶", sweetness="半糖", price=3)
# 呼叫熱飲副函式
print(hot_drink3.modify_name("水之森玄米抹茶"))  # 修改名稱
print(hot_drink3.adjust_sweetness("無糖"))  # 調整甜度
print(hot_drink3.adjust_price(4))  # 調整價錢
print("\n")