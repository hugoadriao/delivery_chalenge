# Delivery Chalenge

## Installation
- Download the project
- Create a venv (optional)
- Execute ```pip install -r requirements.txt```
- Executer ```uvicorn main:app --reload```

## Scenario
- Exist 3 store and 5 deliverymen
- Stores has requests and deliverymen acept those requests
- Deliveryman 4 only acept request from store 1
- Deliverymen can't complain about not having orders
- Every deliverymen has a fix value for request
- Every request has a price
- Every store pay a commission per request
- Deliveryman can have exclusivity with a store
- Deliveryman with exclusivity has priority in requests
- Store can't have exclusivity with a deliveryman
- At the end it has to answer the following questions:
  - Who is the deliveryman and how many requests it has?
  - From wich store is the request?
  - How much the deliveryman will earn?

## Objective
This FastAPI project has 3 routes:
- ```/order_assign```
- ```/bike/{bike_id}``` bike_id: int (1..5)
- ```/bikes```

The route ```/order_assign``` execute a role process where the stores register a request in a 
random order and a deliverymen acept or not the request, therefore, the object of this route
is to give some sort of reality to the actions in this scenario.
The routes ```/bikes``` and ```/bike/{bike_id}``` mimic a scenario
where the distribution of request already happened, therefore, the aim of those
routes is only give a way to access a database.
