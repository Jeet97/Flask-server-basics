from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

base = declarative_base()


class Student_Details(base):
    __tablename__ = 'Students'


    roll_no = Column(Integer,primary_key = True)
    name = Column(String(250),nullable = False)
    

        



engine = create_engine('sqlite:///Students.db')

base.metadata.create_all(engine)
