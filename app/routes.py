# -*- coding: utf-8 -*-

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'дорогой гость'}
    products = [
        {
            'item': {'itemname': 'RaspberryPi'},
            'body': 'single board computer',
            'price': '10'
        },
        {
            'item': {'itemname': 'OrangePi'},
            'body': 'single board computer',
            'price': '8'

        }, 
        {
            'item': {'itemname': 'BeagleBone'},
            'body': 'single board computer',
            'price': '12'
        }
    ]
    return render_template('index.html', title='Home',user=user, products=products)

@app.route('/RaspberryPi')
def RaspberryPi():
    return 'RaspberryPi,,.'

@app.route('/OrangePi')
def OrangePi():
    return '///OrangePi'

@app.route('/BeagleBone')
def BeagleBone():
    return 'BeagleBone...'

@app.route('/explore/<product_name>')
def explore_product(product_name):
    
    return product_name


