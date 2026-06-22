from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = [
    ("Laptop", "Electronics", 50000),
    ("Phone", "Electronics", 25000),
    ("Shoes", "Fashion", 2000),
    ("Watch", "Accessories", 3000)
]

while True:
    product = random.choice(products)

    order = {
        "order_id": random.randint(1000,9999),
        "customer_id": random.randint(100,500),
        "product": product[0],
        "category": product[1],
        "quantity": random.randint(1,5),
        "price": product[2],
        "timestamp": str(datetime.now())
    }

    producer.send("orders", order)
    print(order)

    time.sleep(2)