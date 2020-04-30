# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name : price
   Description :
   Author : wushuangjie
   date : 2020/4/27
-------------------------------------------------
   Change Activity : 2020/4/27
-------------------------------------------------
"""
import cgi

f = cgi.FieldStorage()
shop_price1 = f.getvalue('shopPrice1')
shop_offer1 = f.getvalue('shopOffer1')
shop_price2 = f.getvalue('shopPrice2')
shop_offer2 = f.getvalue('shopOffer2')
shop_price3 = f.getvalue('shopPrice3')
shop_offer3 = f.getvalue('shopOffer3')
net_offer = f.getvalue('netOffer')

sum_price = shop_price1 + shop_price2 + shop_price3
sum_offer = shop_offer1 + shop_offer2 + shop_offer3 + net_offer
real_sum = sum_price - sum_offer

print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
# print ("<meta charset=\"utf-8\">")
print ("<title>比价</title>")
print ("</head>")
print ("<body>")
print (u"<h2> 店铺1价格：%s,店铺优惠： %s</h2>" % (shop_price1, shop_offer1))
print (u"<h2> 店铺2价格：%s,店铺优惠： %s</h2>" % (shop_price2, shop_offer2))
print (u"<h2> 店铺3价格：%s,店铺优惠： %s</h2>" % (shop_price3, shop_offer3))
print (u"<h2> 全网优惠：%s</h2>" % net_offer)
print (u"<h2> h2商品未优惠总价：%s</h2>" % sum_price)
print (u"<h2> 商品总优惠：%s</h2>" % sum_offer)
print (u"<h2> 商品实际总价：%s</h2>" % real_sum)
print ("</body>")
print ("</html>")