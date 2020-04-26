#=====================================
import re
import string


##计算每个价格优惠后的单价

#计算总价，计数，店铺参与优惠类型
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

# def Discount(count_Price):
#     sw = {
#          "299 - 60":count_Price-60,
#          "300 - 40":count_Price-40,
#     }
#     print("优惠方案")
#     for key in sw.keys():
#         print(key)
#     Discount = input("请选择优惠方案:")
#     #返回优惠价格
#     return sw[Discount]


#输入多个优惠方案
def Discount_per():
    Discount = input("请输入优惠方案:")
    if ("-" in Discount)== True:
        print("满减")
        requirement = re.split("-",Discount)
        requirement_height = int(requirement[0])
        requirement_l = int(requirement[1])
        requirement_Discount = int((requirement_height-requirement_l)/requirement_height)
        return requirement_height,requirement_Discount
    elif ("%" in Discount)== True:
        print("打折")
        requirement = re.split("%", Discount)
        requirement_Discount = int(requirement[0])
        return requirement_Discount
    else:
        print("请输入正确方案")
    #print("打折幅度：%d%%"%(requirement_Discount*100))

if __name__ == '__main__':
    try:
        count_Price,Price_Single,n = PriceDiscount()
        sw,max= Discount_per()
        if count_Price > max:
            print("优惠之后价格：", count_Price*sw)
            print("==============================")
            # 计算打折幅度
            #percentage = int(sw) / count_Price
            #print("打折幅度：%d%%" %(percentage*100))
            print("打折幅度：%d%%" % (sw * 100))
            print("==============================")
            for i in range(0, n):
                Price_Single[i] = int(Price_Single[i]) * sw
                print("单价优惠后%.2f" % int(Price_Single[i]))

        else:
            print("不满足优惠条件")
    except ValueError:
        print("输入格式有误")
