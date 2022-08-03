from flask import Flask, jsonify, request
import json
app = Flask(__name__)

DevList = [
    {"name": "João", "hability": ["Python", "Flask"]},
    {"name": "Maria", "hability": ["Python", "Django"]},
    {"name": "Pedro", "hability": ["Python", "Django"]},
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            res = DevList[id]
        except IndexError:
            res = {'status': 'error', 'message': 'Dev not found'}
            return jsonify(res)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        DevList[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        DevList.pop(id)
        return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run(debug=True)
