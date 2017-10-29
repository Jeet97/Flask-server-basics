from functools import wraps
from flask import request, Response, Flask


app = Flask(__name__)
app.debug = True
app.secret_key = 'Your Secret key here'


def check_auth(username, password):
 #This method checks username and password and return true if match found
    return username == 'admin' and password == 'secret'

def authenticate():
    #Returns a 401 response
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/secret-page')
@requires_auth
def secret_page():
    return 'This is something secret!!!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 1234)
