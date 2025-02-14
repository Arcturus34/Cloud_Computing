import pika
import json
import redis


r = redis.Redis(host='localhost', port=6379, db=0)


def calcul(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)


def reception(ch, method, properties, body):

    task = json.loads(body)

    operation_id, num1, num2, operator = task

    result = calcul(num1, num2, operator)

    r.set(operation_id, result)

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1) 
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()

