from flask import Flask, jsonify, request
import json
app = Flask(__name__)

DevList = [
    {"name": "João", "hability": ["Python", "Flask"]},
    {"name": "Maria", "hability": ["Python", "Django"]},
    {"name": "Pedro", "hability": ["Python", "Django"]},
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT'])
def dev(id):
    if request.method == 'GET':
        dev = DevList[id]
        return jsonify(dev)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        DevList[id] = dados
        return jsonify(dados)


if __name__ == '__main__':
    app.run(debug=True)
