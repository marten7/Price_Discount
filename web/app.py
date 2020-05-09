#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: sunjoy
@software: PyCharm
@file: app.py
@time: 2020/5/9 10:24 上午
@description: 
"""

from flask import Flask
from flask import request
from flask import render_template
from pathlib import Path

app = Flask(__name__,
            template_folder=Path.cwd().parent.joinpath('templates'))


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("form.html")


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template("form.html")


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    # password = request.form['password']
    if username == 'admin':
        return render_template('price.html', username=username)
    return render_template('form.html', message='Bad username or password',
                           username=username)


@app.route('/price', methods=['GET'])
def price_input():
    return render_template('price.html')


@app.route('/price', methods=['POST'])
def price_calculate():
    username = "admin"
    shopPrice1 = request.form['shopPrice1']
    shopPrice2 = request.form['shopPrice2']
    shopOffer1 = request.form['shopOffer1']
    shopOffer2 = request.form['shopOffer2']
    netOffer = request.form['netOffer']
    return render_template('price_calculate.html', shopPrice1=shopPrice1,
                           shopPrice2=shopPrice2, shopOffer1=shopOffer1,
                           shopOffer2=shopOffer2, netOffer=netOffer,
                           username=username)


if __name__ == '__main__':
    app.run(debug=True)
