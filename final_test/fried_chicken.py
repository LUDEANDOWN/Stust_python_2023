class FriedChicken:
    def __init__(self, flavor, size, crispy_level, sauce, base_price):
        self.flavor = flavor  # 炸雞口味
        self.size = size  # 炸雞大小
        self.crispy_level = crispy_level  # 酥脆程度
        self.sauce = sauce  # 配料醬汁
        self.base_price = base_price  # 炸雞基本價格

    def calculate_total_price(self):
        # 計算總價格，根據基本價格跟脆度影響總價
        total_price = self.base_price + self.crispy_level
        return total_price

    def display_info(self):
        print(f"炸雞資訊:")
        print(f"炸雞口味: {self.flavor}") # 炸雞口味
        print(f"炸雞大小: {self.size}")# 炸雞大小
        print(f"酥脆程度: {self.crispy_level}")# 酥脆程度
        print(f"配料醬汁: {self.sauce}")# 配料醬汁
        print(f"基本價格: ${self.base_price}")# 炸雞基本價格
        print(f"總價格: ${self.calculate_total_price()}")
        return

    def increase_crispiness(self, increment):
        self.crispy_level += increment# 增加酥脆程度
        if increment<0:
            print(f"脆度減少 {abs(increment)} 個等級.")
        else:
            print(f"再脆度增加 {increment} 個等級.")

    def add_extra_sauce(self, extra_sauce):
        self.sauce += f"+{extra_sauce}"# 增加醬汁
        print(f"額外醬汁 '{extra_sauce}' 加入.")

    def update_base_price(self): #更新最終總價
        print(f"基本價格更新為 ${self.calculate_total_price()}")

#建立4個物件
chicken1 = FriedChicken(flavor="辣味", size="大", crispy_level=3, sauce="烤肉醬", base_price=12) #目前總價12+3=15
chicken1.display_info()
chicken1.increase_crispiness(5) #增加脆度5,所以總價15+5=20
chicken1.add_extra_sauce("美乃滋")
chicken1.update_base_price()#更新價格
print("\n")
chicken2 = FriedChicken(flavor="原味", size="小", crispy_level=4, sauce="起司醬", base_price=10) #目前總價10+4=14
chicken2.display_info()
chicken2.increase_crispiness(2) #增加脆度2,所以總價14+2=16
chicken2.add_extra_sauce("沙茶醬")
chicken2.update_base_price()#更新價格
print("\n")
chicken3 = FriedChicken(flavor="檸檬", size="中", crispy_level=6, sauce="辣醬", base_price=11) #目前總價11+5=17
chicken3.display_info()
chicken3.increase_crispiness(-3) #減少脆度3,所以總價17-3=14
chicken3.add_extra_sauce("果醬")
chicken3.update_base_price()#更新價格
print("\n")
chicken4 = FriedChicken(flavor="巧克力", size="大", crispy_level=8, sauce="果醬", base_price=13) #目前總價13+8=21
chicken4.display_info()
chicken4.increase_crispiness(-5) #減少脆度5,所以總價21-5=16
chicken4.add_extra_sauce("果醬")
chicken4.update_base_price()#更新價格
