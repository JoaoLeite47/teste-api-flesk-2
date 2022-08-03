from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

DevList = [
    {"id": 0, "name": "João", "hability": ["Python", "Flask"]},
    {"id": 1, "name": "Maria", "hability": ["Python", "Django"]},
    {"id": 2, "name": "Pedro", "hability": ["Python", "Django"]},
]


class Dev(Resource):
    def get(self, id):
        try:
            res = DevList[id]
        except IndexError:
            res = {'status': 'error', 'message': 'Dev not found'}
        except Exception:
            res = {'status': 'error', 'message': 'Unexpected error'}
        return(res)

    def put(self):
        dados = json.loads(request.data)
        DevList[id] = dados
        return jsonify(dados)

    def delete(self):
        DevList.pop(id)
        return({"status": "ok"})


class NewDevList(Resource):
    def get(self):
        return(DevList)

    def post(self):
        dados = json.loads(request.data)
        position = len(DevList)
        dados['id'] = position
        DevList.append(dados)
        return (DevList[position])


api.add_resource(Dev, '/dev/<int:id>/')
api.add_resource(NewDevList, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)
