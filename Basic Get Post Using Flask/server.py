from flask import request,render_template,url_for
from Config import session,app,HOST,PORT
from Create_student_table import Student_Details
from sqlalchemy.exc  import SQLAlchemyError

@app.route('/display_details',methods = ['GET','POST'])
def display_student_details():
    if (request.method == 'POST'):
        try:
            roll_no = request.form['roll']
            student = session.query(Student_Details).filter_by(roll_no = roll_no).first()
            if (student):
                return render_template('display_details.html',student = student)
            else:
                return 'No such student found!!'

        except KeyError as k:
            return 'No arguments found in post request'
        

    else:
        return render_template('request_details.html')

@app.route('/add_student',methods = ['GET','POST'])
def add_student():
    if (request.method == 'POST'):
        try:
            name = request.form['name']
            roll_no = request.form['roll']
            student = Student_Details(name = name,roll_no = roll_no)
            session.add(student)
            session.commit()
            return 'You are successfully registered.'
        except KeyError as k:
            return 'No arguments found in post request'



    else:
        return render_template('student_form.html')



if __name__ == '__main__':
    app.run(host = HOST, port = PORT)    
        
        
        
    
    


