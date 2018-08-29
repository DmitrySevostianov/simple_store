# -*- coding: utf-8 -*-

from flask import render_template
from app import app


products = [
        {
            'id': '1',
            'item': {'itemname': 'RaspberryPi'},
            'body': 'single board computer',
            'price': '10'
        },
        {
            'id': '2',
            'item': {'itemname': 'OrangePi'},
            'body': 'single board computer',
            'price': '8'

        }, 
        {
            'id': '3',
            'item': {'itemname': 'BeagleBone'},
            'body': 'single board computer',
            'price': '12'
        }
    ]

products_dict = {
        '1':{
            'id': '1',
            'item': {'itemname': 'RaspberryPi'},
            'body': 'single board computer',
            'price': '10'
        },
        '2':{
            'id': '2',
            'item': {'itemname': 'OrangePi'},
            'body': 'single board computer',
            'price': '8'

        }, 
        '3':{
            'id': '3',
            'item': {'itemname': 'BeagleBone'},
            'body': 'single board computer',
            'price': '12'
        }
    }


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', products=products)


@app.route('/explore/<product_id>')
def explore_product(product_id):
    current_product = {}
    for product in products:
        print (product['id'])
        if product['id'] == product_id:
            current_product = product
            
    print(products_dict[product_id])
    #print('Requsted product: ',current_product)

    return render_template('detail.html', title='Detail', product=current_product)



