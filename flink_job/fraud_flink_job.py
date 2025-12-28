from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import KafkaSource, KafkaSink, KafkaRecordSerializationSchema
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types
import json
import pickle
import xgboost as xgb

model = pickle.load(open("fraud_model.pkl", "rb"))

env = StreamExecutionEnvironment.get_execution_environment()

source = KafkaSource.builder() \
    .set_bootstrap_servers("kafka:9092") \
    .set_topics("transactions") \
    .set_group_id("fraud-group") \
    .set_value_only_deserializer(SimpleStringSchema()) \
    .build()

env.from_source(source, watermark_strategy=None, source_name="Kafka Source") \
    .map(lambda x: json.loads(x), output_type=Types.MAP(Types.STRING, Types.STRING)) \
    .map(lambda txn: predict(txn)) \
    .filter(lambda res: res["is_fraud"]) \
    .map(lambda x: json.dumps(x)) \
    .sink_to(
        KafkaSink.builder()
        .set_bootstrap_servers("kafka:9092")
        .set_record_serializer(
            KafkaRecordSerializationSchema.builder()
            .set_topic("fraud_alerts")
            .set_value_serialization_schema(SimpleStringSchema())
            .build()
        ).build()
    )

def predict(txn):
    data = [[float(txn["amount"]), float(txn["device_score"]), float(txn["user_id"])]]
    pred = model.predict(data)[0]

    txn["is_fraud"] = bool(pred)
    return txn

env.execute("Fraud Detection Job")
