from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'language_platform',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='language_consumer_group',
    value_deserializer=lambda m: m.decode('utf-8')
)

def validate_message(message):
    required_keys = ["user", "language", "lesson", "exercise", "progress_percent", "timestamp"]
    try:
        data = json.loads(message)
    except json.JSONDecodeError:
        return False, message

    for key in required_keys:
        if key not in data:
            return False, message

    if not (0 <= data["progress_percent"] <= 100):
        return False, message

    return True, data

for msg in consumer:
    is_valid, output = validate_message(msg.value)
    if is_valid:
        print(f"VALID: {output}")
    else:
        print(f"NOT VALID: {output}")