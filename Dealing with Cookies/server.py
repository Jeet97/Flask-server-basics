from http import cookie
from flask import Flask, session, redirect, url_for, escape, request


app = Flask(__name__)

@app.route('/welcome')
def cookie_insertion():
    response = current_app.make_response(redirect_to_index )  
    response.set_cookie('cookie_name',value='values')
    return response



    
@app.route('/login')
def cookie_get():
    cookie = request.cookie.get('cookie_name')
    return 'hey user, your cookie is %s',cookie
        

# set the secret key.  keep this really secret:
app.secret_key = 'Your Secret Key Here'


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 1234)
