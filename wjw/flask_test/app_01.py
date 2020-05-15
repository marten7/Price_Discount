from flask import Flask,request,render_template
import re


app = Flask(__name__)
@app.route('/price',methods=['get'])
def home():
    return render_template('price.html')

@app.route('/price',methods=['post'])
def count():
    price1= request.form['prices_01']
    return render_template('price.html',count=price1)

if __name__ == '__main__':
    app.run(port = 3333,debug = True)


