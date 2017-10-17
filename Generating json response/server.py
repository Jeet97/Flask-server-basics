from flask import request,render_template,url_for,jsonify
from Config import session,app,HOST,PORT
from Create_student_table import Student_Details
from sqlalchemy.exc  import SQLAlchemyError

@app.route('/display_all')
def display_all():
        try:
            students = session.query(Student_Details).all()
            if (students):
                return jsonify(Student_Details = [student.serialize for student in students])
            else:
                return 'No Data found!!'

        except KeyError as k:
            return 'Exception Occured'


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
        
        
        
    
    


