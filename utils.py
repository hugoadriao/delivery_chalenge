# @Author: Hugo Silva
# @Date: 05/12/2021
# @File: utils.py
import random

bike_ids = []


def get_random_id(all_stores: int = None,
                  all_bikes: dict = None) -> int:
    if all_stores:
        rand_id = random.randint(0, all_stores - 1)
    else:
        all_bikes_ids = remove_fat_bikes(all_bikes)
        rand_id = random.choice(all_bikes_ids)

    return rand_id


def register_operation(bikes: dict, order: dict, bike_id: str) -> dict:
    bike = bikes.get(bike_id)
    bike['log_operations'].append(order)
    bike['money'] += define_bike_cash_in(order, bike)

    bikes[bike_id] = bike

    return bikes


def bike_accepted() -> str:
    return random.choice(['yes', 'no'])


def bike_accepted_and_respect_exclusivity(bike: dict, order) -> bool:
    respect_exclusivity = respect_bike_exclusivity(bike, order)
    bike_answer = bike_accepted()

    if respect_exclusivity and bike_answer == 'yes':
        sort_another_bike = False
    else:
        sort_another_bike = True

    return sort_another_bike


def remove_fat_bikes(all_bikes: dict):
    all_bikes_id = list(all_bikes.keys())
    for bike in all_bikes:
        if len(all_bikes.get(bike).get('log_operations')) >= 2:
            all_bikes_id.remove(bike)
    return all_bikes_id


def bike_accept_request(
        bikes: dict,
        order: dict
) -> dict:
    priority_id = order.get('priority')
    if bike_accepted() == 'yes' and priority_id:
        bikes = register_operation(bikes, order, priority_id)
    else:
        bike_id = get_random_id(all_bikes=bikes)
        while (
                bike_accepted_and_respect_exclusivity(
                    bikes.get(bike_id), order
                )
        ):
            bike_id = get_random_id(all_bikes=bikes)
        bikes = register_operation(bikes, order, bike_id)

    return bikes


def respect_bike_exclusivity(bike: dict, order: dict) -> bool:
    bike_exclusivity = bike.get('exclusivity')
    if bike_exclusivity:
        if bike_exclusivity == order.get('store_id'):
            condition = True
        else:
            condition = False
    else:
        condition = True

    return condition


def define_bike_cash_in(order: dict, bike: dict) -> float:
    order_value = order.get('value')
    store_comission = order.get('commission')
    bike_fixed_value = bike.get('fixed_value')

    return order_value * (store_comission / 100) + bike_fixed_value


def assign_priority_order(bikes: list, orders: list):
    orders_copy = orders[:]
    priority_orders = []
    for order in orders:
        if order.get('priority'):
            orders_copy.remove(order)
            order['rejected_times'] = 0
            priority_orders.append(order)

    while len(priority_orders) >= 1:
        for order in priority_orders:
            if bike_accepted() == 'yes':
                bikes = register_operation(
                    bikes, order, order.get('priority')
                )
                priority_orders.remove(order)
            else:
                order['rejected_times'] += 1

            if order['rejected_times'] >= 2:
                orders_copy.append(order)
                priority_orders.remove(order)

    if len(priority_orders) > 0:
        orders_copy = orders_copy + priority_orders
    return bikes, orders_copy


def shuffle_orders(stores: []) -> {}:
    orders_list = []
    while True:
        rand_index = get_random_id(len(stores))
        if len(stores[rand_index]['orders']) >= 1:
            orders_list.append(
                {
                    "store_id": stores[rand_index].get('id'),
                    "value": stores[rand_index].
                        get('orders')[0].get('value'),
                    "commission": stores[rand_index].get('commission'),
                    "priority": stores[rand_index].get('priority')
                }
            )
            stores[rand_index].get('orders').pop(0)
        else:
            stores.pop(rand_index)
            if len(stores) < 1:
                break

    return orders_list


def build_pretty_log(logs: [dict]) -> [dict]:
    pretty_logs = []
    order_id = 0
    for item in logs:
        pretty_logs.append(
            {
                'pedido_id': order_id,
                'loja': item.get('store_id'),
                'valor_pedido': item.get('value')
            }
        )
        order_id += 1
    del order_id
    return pretty_logs


def build_response(bikes: dict) -> dict:
    response = {}
    for bike in bikes:
        response[bike] = {
            'pedidos': build_pretty_log(
                bikes.get(bike).get('log_operations')
            ),
            'cash_in': bikes.get(bike).get('money')
        }
    return response
