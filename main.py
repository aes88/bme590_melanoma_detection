from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test')
def hello_world():
    return 'Hello, world2'

@app.route('/', methods=['POST'])
def validate():
        img = request.get_json()
        img_string = img['image']
        str = "received"
        return str
