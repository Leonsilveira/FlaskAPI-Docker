from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de itens populares (exemplo)
popular_items = [
    {"item_id": 1, "name": "Item A", "popularity_score": 95},
    {"item_id": 2, "name": "Item B", "popularity_score": 90},
    {"item_id": 3, "name": "Item C", "popularity_score": 85},
    {"item_id": 4, "name": "Item D", "popularity_score": 80},
    {"item_id": 5, "name": "Item E", "popularity_score": 75}
]

@app.route('/recommend', methods=['POST'])
def recommend():
    if not request.is_json:
        return jsonify({'error': 'Request body must be JSON'}), 400

    data = request.get_json(force=True)

    if 'features' not in data:
        return jsonify({'error': 'No features provided'}), 400

    if not isinstance(data['features'], list) or any(x is None for x in data['features']):
        return jsonify({'error': 'Invalid features'}), 400

    recommendations = popular_items[:5]  # Exemplo: pegar os 5 itens mais populares

    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Garanta que a aplicação ouça em todas as interfaces
