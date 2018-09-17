from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def status():
    return 'hello to you', 200


@app.route('/add', methods=['POST'])
def add():
    d = request.json
    a = int(d['a'])
    b = int(d['b'])
    return str(a + b), 200

app.run(host='0.0.0.0')
