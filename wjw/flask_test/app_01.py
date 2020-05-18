from flask import Flask,request,render_template
from Price_Discount.wjw.flask_test import count

app = Flask(__name__)
@app.route('/price',methods=['get'])
def home():
    return render_template('price.html')

@app.route('/price',methods=['post'])
def count():
    try:
        prices1_list= request.form['prices_01']
        count_Price,Price_Single,n =count.PriceCount(prices1_list)
        Single_list = ''
        for i in range(0,n):
            Single_list += str(Price_Single[i])
            Single_list += '<br>'

        return render_template('price.html',count=count_Price,price=Single_list)
    except ValueError:
        return render_template('price.html',message='请输入正确价格!')



if __name__ == '__main__':
    app.run(port = 3333,debug = True)


