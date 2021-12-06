# @Author: Hugo Silva
# @Date: 04/12/2021
# @File: main.py
import copy
import json

from fastapi import FastAPI

import db
from utils import (shuffle_orders, bike_accept_request,
                   assign_priority_order, build_response)

app = FastAPI()


@app.get("/api/v1/order_assign/")
def order_assign():
    stores = copy.deepcopy(db.stores.get('stores'))
    bikes = copy.deepcopy(db.bikes_id)

    orders_list = shuffle_orders(stores)

    bikes, orders_list = assign_priority_order(bikes, orders_list)

    for order in orders_list:
        bikes = bike_accept_request(bikes, order)

    return build_response(bikes)


@app.get("/api/v1/bike/{bike_id}")
def get_bike(bike_id):
    with open('result.json') as data_base:
        data = json.load(data_base)

    return {f'Moto {bike_id}': data.get(f'Moto {bike_id}')}


@app.get("/api/v1/bikes/")
def get_bikes():
    with open('result.json') as data_base:
        return json.load(data_base)
