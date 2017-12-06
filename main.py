from flask import Flask, request, jsonify
from flask_cors import CORS
from time import gmtime, strftime
import base64
import re

app = Flask(__name__)
CORS(app)

@app.route('/test')
def hello_world():
    return 'Hello, world2'

@app.route('/', methods=['POST'])
def validate():
        img = request.get_json()
        img_string = img['image']
	filename = strftime("%Y%m%d_%H_%M_%S", gmtime())
	PATH = "images/"
	file_ending = ".jpg"
	filepath = PATH + filename + file_ending
	with open (filepath, "w") as image_out:
		image_out.write(re.sub('^data:image/.+;base64,', '', img_string).decode('base64'))
        str = "received"
        return str
