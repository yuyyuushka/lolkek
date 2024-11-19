from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        data = request.json
        print("Полученные данные (POST):", data)
        return jsonify(data), 201
    elif request.method == 'GET':
        params = request.args
        print("Полученные параметры (GET):", params)
        return jsonify(params), 200

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
