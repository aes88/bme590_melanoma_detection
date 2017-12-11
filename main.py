from flask import Flask, request, jsonify
from flask_cors import CORS
from time import gmtime, strftime
import base64
import re
from setup_db import User, write_file
from melanomapredictions import predict

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
	check_jpg = re.search("^data:image/jpeg",img_string)
	if (check_jpg != None):
		file_ending = ".jpg"
	else:
		check_png = re.search("^data:image/png", img_string)
		if (check_png != None):
			file_ending = ".png"
		else:
			check_gif = re.search("^data:image/gif", img_string)
			if (check_gif != None):
				file_ending = ".gif"
			else:
				error_string = "Error: Incorrect file type uploaded"
				return error_string
	filepath = PATH + filename + file_ending
	with open (filepath, "w") as image_out:
		image_out.write(re.sub('^data:image/.+;base64,', '', img_string).decode('base64'))
        labels, predictions = predict(filepath)
	name = "test"
	malignant = 0
	benign = 0
	symmetry = 0
	border = 0
	color = 0
	diameter = 1
	predict2 = predictions.tolist()
	labels2 = str(labels) 
	predict3 = str(predict2)
	results = {"labels": labels2, "probabilities": predict3}
	write_file(name,file_ending,filepath,malignant,benign,symmetry,border,color,diameter)
        return str(results)
