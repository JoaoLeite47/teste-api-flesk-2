from flask import Flask, jsonify

app = Flask(__name__)

DevList = [
    {"name": "João", "hability": ["Python", "Flask"]},
    {"name": "Maria", "hability": ["Python", "Django"]},
    {"name": "Pedro", "hability": ["Python", "Django"]},
]


@app.route('/dev/<int:id>/')
def dev(id):
    dev = DevList[id]
    return jsonify(dev)


if __name__ == '__main__':
    app.run(debug=True)
