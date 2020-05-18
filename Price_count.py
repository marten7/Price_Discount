import re

def PriceCount(prices_list):
    n = 0
    count_Price = 0
    #多分隔：以空格、英文逗号、中文逗号
    Price_Single = re.split(",| |，",prices_list)
    #计算总价
    for price in Price_Single:
        count_Price +=int(price)
        n+=1
    #返回总价、单价、商品数量
    return count_Price,Price_Single,n
