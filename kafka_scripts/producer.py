from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

while True:
    txn = {
        "transaction_id": random.randint(1000, 9999),
        "user_id": random.randint(1, 50),
        "amount": random.uniform(10, 5000),
        "location": random.choice(["US", "IN", "UK", "CN"]),
        "device_score": random.uniform(0, 1)
    }

    producer.send("transactions", txn)
    print("Sent:", txn)
    time.sleep(1)
