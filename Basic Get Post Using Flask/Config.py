from flask import Flask
from Create_student_table import Student_Details,base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



engine = create_engine(r'sqlite:///Students.db')
base.metadata.bind = engine
dbsession = sessionmaker(engine)
session = dbsession()

app = Flask(__name__)
app.secrete_key = 'YOUR SECRET KEY HERE'
app.debug = True

HOST = '0.0.0.0' # Your machine's ip address here.
PORT = 2323 # Desired port no. for your process(i.e your server).
