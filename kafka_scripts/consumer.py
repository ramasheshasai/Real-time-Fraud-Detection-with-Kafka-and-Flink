from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "fraud_alerts",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Listening for fraud alerts...")

for msg in consumer:
    print("⚠ FRAUD DETECTED:", msg.value)
    