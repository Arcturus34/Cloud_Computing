from flask import Flask, request, jsonify
import uuid
import redis
import pika
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    if 'num1' not in data or 'num2' not in data or 'operator' not in data:
        return jsonify({'error':'Données manquantes'}), 400
    
    num1 = data['num1']
    num2 = data['num2']
    operator = data['operator']
    
    try:
        operation_id = operation_id = r.incr('counter')

        operation_tuple = (operation_id, num1, num2, operator)

        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='task_queue', durable=True)

        message = json.dumps(operation_tuple)

        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
        connection.close()
        return jsonify({'operation_id': operation_id})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/result/<operation_id>', methods=['GET'])
def get_result(operation_id):
    result = r.get(operation_id)

    if result is not None:
        return jsonify({'result': result})

    return jsonify({'error': 'ID non trouvé'}), 404


if __name__ == '__main__':
    app.run(debug=True)

