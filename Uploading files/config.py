from flask import Flask



app = Flask(__name__)
app.secrete_key = 'YOUR SECRET KEY HERE'
app.debug = True

HOST = '0.0.0.0' # Your machine's ip address here.
PORT = 2323 # Desired port no. for your process(i.e your server).
UPLOAD_FOLDER = 'FULL DIRECTORY PATH OF UPLOAD FOLDER'

exts = set(['jpg','jpeg','txt','pdf','mp4','mp3']) # Here you can control the kind of file to be uploaded. These are the file type that are allowed.
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
