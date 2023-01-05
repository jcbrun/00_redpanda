# streaming_worker.py
from kafka import KafkaConsumer
from time import sleep

def process_message(email):
    print(f"SIMULATION : sending email to {email}")
    sleep(1) # pretend to do work
    print("finished processing message")
    print("==== "*10)
    
if __name__ == "__main__":
    print("starting streaming consumer app")
    consumer = KafkaConsumer(
        'user_signups',
        bootstrap_servers=["localhost:9092"],
        group_id="group1"
    )
    
    for message in consumer:
        process_message(message.value)
        print(f"offset, key, value > ", message.offset, message.key, message.value)
