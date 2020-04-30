from pythonproject.Price_Disconunt import Price_count
from pythonproject.Price_Disconunt import Sale

if __name__ == '__main__':
    try:
        count_Price, Price_Single, n = Price_count.PriceDiscount()
        saleway = input("请输入优惠方式")
        if ("-" in saleway)== True:
            requirement_height, requirement_Discount= Sale.sale.FullReduction(saleway)
            if count_Price>=requirement_height:
                print("优惠后的价格是：",count_Price-requirement_Discount)
            else:
                print("不满足优惠条件，当前总价是：",count_Price)

        # elif ("%" in sale)== True:

        else:
            print("请输入正确方案")

        #
        # if count_Price > max:
        #     print("优惠之后价格：", count_Price*sw)
        #     print("==============================")
        #     # 计算打折幅度
        #     #percentage = int(sw) / count_Price
        #     #print("打折幅度：%d%%" %(percentage*100))
        #     print("打折幅度：%d%%" % (sw * 100))
        #     print("==============================")
        #     for i in range(0, n):
        #         Price_Single[i] = int(Price_Single[i]) * sw
        #         print("单价优惠后%.2f" % int(Price_Single[i]))

     except ValueError:
        print("输入格式有误")