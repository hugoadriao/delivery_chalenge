# @Author: Hugo Silva
# @Date: 05/12/2021
# @File: db.py

stores = {
    "stores": [
        {
            "id": 1,
            "orders": [
                {
                    "id": 1,
                    "value": 50.0
                },
                {
                    "id": 2,
                    "value": 50.0
                },
                {
                    "id": 3,
                    "value": 50.0
                }
            ],
            "commission": 5.0,
            "priority": 'Moto 4'
        },
        {
            "id": 2,
            "orders": [
                {
                    "id": 1,
                    "value": 50.0
                },
                {
                    "id": 2,
                    "value": 50.0
                },
                {
                    "id": 3,
                    "value": 50.0
                },
                {
                    "id": 4,
                    "value": 50.0
                }
            ],
            "commission": 5.0
        },
        {
            "id": 3,
            "orders": [
                {
                    "id": 1,
                    "value": 50.0
                },
                {
                    "id": 2,
                    "value": 50.0
                },
                {
                    "id": 3,
                    "value": 100.0
                }
            ],
            "commission": 15.0
        }
    ]
}

bikes = {
    "bikes": [
        {
            "id": 1,
            "fixed_value": 2.0,
            "log_operations": [],
            "money": 0.0,
            "weight": 5.0
        },
        {
            "id": 2,
            "fixed_value": 2.0,
            "log_operations": [],
            "money": 0.0,
            "weight": 5.0
        },
        {
            "id": 3,
            "fixed_value": 2.0,
            "log_operations": [],
            "money": 0.0,
            "weight": 5.0
        },
        {
            "id": 4,
            "fixed_value": 2.0,
            "log_operations": [],
            "money": 0.0,
            "weight": 5.0
        },
        {
            "id": 5,
            "fixed_value": 3.0,
            "log_operations": [],
            "money": 0.0,
            "weight": 5.0
        }
    ]
}

bikes_id = {
    "Moto 1": {
        "fixed_value": 2.0,
        "log_operations": [],
        "money": 0.0
    },
    "Moto 2": {
        "fixed_value": 2.0,
        "log_operations": [],
        "money": 0.0
    },
    "Moto 3": {
        "fixed_value": 2.0,
        "log_operations": [],
        "money": 0.0
    },
    "Moto 4": {
        "fixed_value": 2.0,
        "log_operations": [],
        "money": 0.0,
        "exclusivity": 1
    },
    "Moto 5": {
        "fixed_value": 3.0,
        "log_operations": [],
        "money": 0.0
    }
}
