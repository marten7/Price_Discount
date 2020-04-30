import re

def PriceDiscount():
    #输入多个价格
    listPrice = input("请输入价格，多个价格请用逗号或者空格分隔开：")
    #
    shop_type = input("请输入店铺参与的优惠类型（1：满减、2：打折、3：满减之后打折、4：打折之后满减、5：）：")
    count_Price = 0
    n = 0
    #多分隔：以空格、英文逗号、中文逗号
    Price_Single = re.split(",| |，",listPrice)
    #计算总价
    for price in Price_Single:
        count_Price +=int(price)
        n+=1
    print(n,"件商品总价：",count_Price)
    print("==============================")
    #返回总价、单价、商品数量
    return count_Price,Price_Single,n,shop_type
