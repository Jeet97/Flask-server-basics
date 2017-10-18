from config import HOST,PORT,app,exts
from flask import request,redirect,render_template,send_from_directory,url_for
from werkzeug.utils import secure_filename
import os




def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in exts              # allowed_file method checks if extension of uploaded file matches with one of our  allowed extensions in config.py file.


@app.route('/upload_file',methods =  ['GET','POST'])
def upload_file():
    try:
        
        if request.method == 'POST':
            if 'file' not in request.files:
                return render_template('error.html',message = 'An error occured while uploading file. Please try again.')       # returns error template if entity named as 'file' not found in post request files.

            file = request.files['file']

            if file.filename == '':
                return render_template('error.html', message = 'Empty filenames are not allowed!!!')                            # returns error template if filename is empty.

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)           # To avoid dangerous filename such as .bashrc etc.
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                return redirect(url_for('display_uploaded',filename = filename))
               


        else :
            return render_template('fileupload.html')


            
    except Exception as e:
        return render_template('error.html', message = repr(e))


@app.route('/uploads/<filename>')
def display_uploaded(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'],filename)   # To display uploaded file on server.



if __name__ == '__main__':
    app.run(host = HOST,port = PORT)
