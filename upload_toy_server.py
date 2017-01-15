from flask import Flask,request
from scipy import misc
from sklearn.externals import joblib

import sys
sys.path.append('../')
from DigitClassifier import DigitClassifier


app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
	image_path = request.files['file']
	dc = DigitClassifier("CNN")
	# Load trained model
	model = dc.load_model()
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

	# evaluate loaded model on test data
	#image_path = 'data/test/4391.png'
	predicted_label = dc.predict_image(image_path, model)
	print "Prediction with loaded model for image: ", image_path, " is: ",predicted_label, request.files['file']
	return 'predict: %s ' % (predicted_label[0])


@app.route('/')
def index():
	return '''
    	<!doctype html>
    	<html>
    	<body>
    	<form action='/upload' method='post' enctype='multipart/form-data'>
      		<input type='file' name='file'>
        	<input type='submit' value='Upload'>
    	</form>
    	'''


if __name__ == '__main__':
	"""
    In order to not restart the local server after each change to your code, if you enable debug
    support the server will reload itself on code changes, and provide a debugger. To enable it,
    before running the server:
    $ export FLASK_DEBUG=1
    $ flask run
    or, app.run(threaded=True) allows stopping the server with ctr-c
    """
	# with app.test_request_context():
	# 	print url_for('index')
    #     print url_for('login')
    #     print url_for('login', next='/')
    #     print url_for('profile', username='John Doe')
    #     print url_for('static', filename='style.css')

	app.run()#threaded=True)#, host="0.0.0.0")
