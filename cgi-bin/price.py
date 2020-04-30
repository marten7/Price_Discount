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
shop_price = f.getvalue('shopPrice')
shop_offer = f.getvalue('shopOffer')
net_offer = f.getvalue('netOffer')

print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
# print ("<meta charset=\"utf-8\">")
print ("<title>price compare</title>")
print ("</head>")
print ("<body>")
print (u"<h2> 店铺价格：%s,店铺优惠： %s，全网优惠：%s</h2>" % (shop_price, shop_offer, net_offer))
print ("</body>")
print ("</html>")