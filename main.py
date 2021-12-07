# @Author: Hugo Silva
# @Date: 04/12/2021
# @File: main.py
import copy
import json

from fastapi import FastAPI

import db
from utils import (shuffle_orders, bike_accept_request,
                   assign_priority_order, build_response)

description = """
## **This project is focused in solve a specific problem and has two scenario:**
### Scenarios:
* The more simple where the user only want to get pre-existing data from db. This case use the routes ```/bike/{bike_id}``` and ```/bikes```
* The more complex consider a scenario where the bikes has the option to accept or not the request that randomly arrive. This case use ```order_assign``` and it randomly generates the order of requests and solve the problem every time the route is called.
"""

tags_metadata = [
    {
        'name': 'complex-scenario',
        'description': 'Simulates a simple "real world" to a specific scenario'
    },
    {
        'name': 'get-bike-id',
        'description': 'Get a specific bike from a pre-existing database where the problem is solved'
    },
    {
        'name': 'get-all-bikes',
        'description': 'Get all bikes from a pre-existing database where the problem is solved'
    }
]

app = FastAPI(
    title="Delivery Challenge",
    description=description,
    version="0.0.10",
    openapi_tags=tags_metadata,
    contact={
        'name': 'You can find the source code here',
        'url': 'https://github.com/hugoadriao/delivery_chalenge'
    }
)


@app.get("/api/v1/order_assign/", tags=['complex-scenario'])
def order_assign():
    """
    This end-point simulates a simple world where the request arrive in
    a random order and the bikes chose to accept or not some request
    """
    stores = copy.deepcopy(db.stores.get('stores'))
    bikes = copy.deepcopy(db.bikes_id)

    orders_list = shuffle_orders(stores)

    bikes, orders_list = assign_priority_order(bikes, orders_list)

    for order in orders_list:
        bikes = bike_accept_request(bikes, order)

    return build_response(bikes)


@app.get("/api/v1/bike/{bike_id}", tags=['get-bike-id'])
def get_bike(bike_id: int):
    """
    This end-point return a specific bike by it's ID.
    bike_id -> int (1...5)
    """
    with open('result.json') as data_base:
        data = json.load(data_base)

    return {f'Moto {bike_id}': data.get(f'Moto {bike_id}')}


@app.get("/api/v1/bikes/", tags=['get-all-bikes'])
def get_bikes():
    """
    This end-point return all bikes from database
    """
    with open('result.json') as data_base:
        return json.load(data_base)
