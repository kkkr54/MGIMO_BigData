from kafka import KafkaProducer
from message_generator import generate_message

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: v.encode('utf-8') 
)

topic = "language_platform"

def send_message():
    message = generate_message()
    print(f"Generated message: {message}")
    producer.send(topic, message)
    producer.flush()

if __name__ == "__main__":
    for _ in range(3):  # генерируем x сообщений
        send_message()