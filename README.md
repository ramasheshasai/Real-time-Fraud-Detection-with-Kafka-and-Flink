# 🚀 Real-Time Fraud Detection using Apache Kafka, Apache Flink & Machine Learning

## 🧠 Project Overview
This project builds a real-time fraud detection pipeline where live financial transaction streams are processed using Apache Kafka and Apache Flink, and evaluated using a Machine Learning (XGBoost) model. Suspicious transactions are immediately flagged and pushed into a separate Kafka topic as alerts. This simulates real-world banking, credit card, and UPI fraud detection systems.

---

## 🎯 Objectives
- Stream continuous real-time transactions using Kafka
- Process and analyze streaming data using Apache Flink
- Perform ML-based fraud detection using XGBoost
- Instantly route fraudulent transactions to alerts topic
- Monitor throughput, latency, and performance metrics via Flink Dashboard

---

## 🏗️ System Architecture
Transaction Generator → Kafka (transactions topic)  
→ Apache Flink (Preprocessing + ML Inference)  
→ Fraud? YES → Kafka fraud_alerts topic  
→ Consumer receives alerts in real-time  

---

## 🛠️ Technologies Used
- Apache Kafka
- Apache Flink (PyFlink)
- Python
- XGBoost
- Docker & Docker Compose

---

## 📂 Folder Structure
real-time-fraud-detection/  
├── docker-compose.yml  
├── model/  
│   ├── train_model.py  
│   └── fraud_model.pkl  
├── flink_job/  
│   └── fraud_flink_job.py  
├── kafka_scripts/  
│   ├── producer.py  
│   └── consumer.py  
└── README.md  

---

# ⚙️ Setup & Execution Guide

---

## ✅ Step 1: Install Requirements
Ensure you have installed:
- Docker Desktop
- Python 3.x

Install Python libraries:
```
pip install kafka-python apache-flink xgboost
```

---

## ✅ Step 2: Start Kafka & Flink
Run inside project root:
```
docker compose up -d
```

Open Flink Dashboard:
```
http://localhost:8081
```

---

## ✅ Step 3: Create Kafka Topics
Run:
```
docker exec -it kafka bash
kafka-topics --create --topic transactions --bootstrap-server kafka:9092
kafka-topics --create --topic fraud_alerts --bootstrap-server kafka:9092
exit
```

---

## ✅ Step 4: Train the Machine Learning Model
```
cd model
python train_model.py
cd ..
```

This generates:
```
fraud_model.pkl
```

---

## ✅ Step 5: Copy Files to Flink Container
```
docker cp flink_job/fraud_flink_job.py jobmanager:/fraud_flink_job.py
docker cp model/fraud_model.pkl jobmanager:/fraud_model.pkl
```

---

## ✅ Step 6: Run Flink Streaming Job
```
docker exec -it jobmanager bash
flink run -py /fraud_flink_job.py
```

(Keep this running)

---

## ✅ Step 7: Start Transaction Producer
```
cd kafka_scripts
python producer.py
```

---

## ✅ Step 8: Start Fraud Alert Consumer
```
python consumer.py
```

Fraud alerts display like:
```
⚠ FRAUD DETECTED: { transaction_details_here }
```

---

# 📊 Monitoring & Metrics
Open Dashboard:
```
http://localhost:8081
```

Monitor:
- Real-time throughput
- Latency
- Execution graph
- Backpressure

---

# 🧪 Expected Output
- Kafka streams continuous transactions
- Flink processes in real time
- ML model predicts fraud probability
- Fraud transactions sent to `fraud_alerts`
- Consumer prints alerts instantly

---

# 📈 Example Performance Summary (For Report)
- Processes ~1200 transactions/min
- Average latency ~200–300 ms
- Stable streaming with minimal backpressure
- Instant fraud alerts

---

# 🏁 Conclusion
This project demonstrates a production-style real-time streaming fraud detection pipeline using Apache Kafka, Apache Flink, and Machine Learning. It showcases real-time data pipelines, distributed stream processing, ML deployment, monitoring, and scalable architecture used in modern fintech systems.

---

# 👨‍💻 Author
**rama shesha sai satuluri**
