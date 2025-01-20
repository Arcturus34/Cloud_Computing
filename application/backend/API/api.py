from flask import Flask, request, jsonify

app = Flask(__name__)

# Stocker les résultats dans un dictionnaire
calculs = {}
id_compteur = 1

@app.route('/api/v1/calculate', methods=['POST'])
def calculer():
    global id_compteur
    data = request.get_json()

    # Vérification des données
    if not data or 'operation' not in data or 'nombres' not in data:
        return jsonify({"erreur": "Requête invalide. Fournissez 'operation' et 'nombres'."}), 400

    operation = data['operation']
    nombres = data['nombres']

    if not isinstance(nombres, (list, tuple)) or len(nombres) != 2:
        return jsonify({"erreur": "Il faut 2 nombres"}), 400

    try:
        num1, num2 = float(nombres[0]), float(nombres[1])
    except ValueError:
        return jsonify({"erreur": "Il faut des nombres"}), 400

    # Effectuer le calcul
    try:
        if operation == 'addition':
            resultat = num1 + num2
        elif operation == 'soustraction':
            resultat = num1 - num2
        elif operation == 'multiplication':
            resultat = num1 * num2
        elif operation == 'division':
            if num2 == 0:
                return jsonify({"erreur": "La division par zéro n'est pas autorisée."}), 400
            resultat = num1 / num2
        else:
            return jsonify({"erreur": "Opération invalide. Les opérations supportées sont : addition, soustraction, multiplication, division."}), 400
    except Exception as e:
        return jsonify({"erreur": f"Une erreur est survenue : {str(e)}"}), 500

    # Sauvegarder le résultat
    id_operation = id_compteur
    calculs[id_operation] = resultat
    id_compteur += 1

    return jsonify({"id": id_operation}), 201


@app.route('/api/v1/result/<int:id_operation>', methods=['GET'])
def obtenir_resultat(id_operation):
    # Récupérer le résultat
    resultat = calculs.get(id_operation)
    if resultat is None:
        return jsonify({"erreur": "ID d'opération non trouvé."}), 404

    return jsonify({"id": id_operation, "resultat": resultat}), 200


if __name__ == '__main__':
    app.run(debug=True)

