from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Stockage des résultats en mémoire
calculations = {}

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    if 'num1' not in data or 'num2' not in data or 'operator' not in data:
        return jsonify({'error': 'Données manquantes'}), 400
    
    num1 = data['num1']
    num2 = data['num2']
    operator = data['operator']
    
    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return jsonify({'error': 'Division par zéro'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Opérateur non valide'}), 400
        
        operation_id = str(uuid.uuid4())
        calculations[operation_id] = result
        return jsonify({'operation_id': operation_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/result/<operation_id>', methods=['GET'])
def get_result(operation_id):
    if operation_id in calculations:
        return jsonify({'result': calculations[operation_id]})
    return jsonify({'error': 'ID non trouvé'}), 404

if __name__ == '__main__':
    app.run(debug=True)
