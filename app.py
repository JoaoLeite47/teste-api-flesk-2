from flask import Flask, jsonify, request
import json
app = Flask(__name__)

DevList = [
    {"id": 0, "name": "João", "hability": ["Python", "Flask"]},
    {"id": 1, "name": "Maria", "hability": ["Python", "Django"]},
    {"id": 2, "name": "Pedro", "hability": ["Python", "Django"]},
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            res = DevList[id]
        except IndexError:
            res = {'status': 'error', 'message': 'Dev not found'}
        except Exception:
            res = {'status': 'error', 'message': 'Unexpected error'}
        return jsonify(res)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        DevList[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        DevList.pop(id)
        return jsonify({"status": "ok"})


@app.route('/dev/', methods=['POST'])
def NewDevList():
    if request.method == 'POST':
        dados = json.loads(request.data)
        position = len(DevList)
        dados['id'] = position
        DevList.append(dados)
        return jsonify(DevList[position])


if __name__ == '__main__':
    app.run(debug=True)
