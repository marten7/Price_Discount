import re

class sale():
    #满减 返回 【条件】 和 【优惠金额】
    def FullReduction(self,sale):
        self.sale = sale
        print("满减")
        requirement = re.split("-", self.sale)
        requirement_height = int(requirement[0])
        requirement_l = int(requirement[1])
        requirement_Discount = int((requirement_height - requirement_l) / requirement_height)
        return requirement_height, requirement_Discount
    #打折 返回 【打折小数】
    def Discount(self,sale):
        self.sale = sale
        print("打折")
        requirement = re.split("%", self.sale)
        requirement_Discount = int(requirement[0])
        return requirement_Discount
