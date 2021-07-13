from flask import Flask
from flask import request
import jwt
import time

app = Flask(__name__)

users = [
    {
        'username': 'david',
        'password': 'ghostbusters'
    },
    {
        'username': 'billmurray',
        'password': 'ghostbusters'
    }
]

@app.route("/jwt-token")
def jwt_issuer():
    username = request.args.get('username')
    password = request.args.get('password')
    # match the username and password against sources
    for user in users:
        if user['username'] == username and user['password'] == password:
            now = int(time.time())
            return jwt.encode({'application': "jwt-issuer"}, "my-super-super-secret", algorithm="HS256", headers = {"iss": username, "iat": now, "exp": now + 300})
            
    return {'status': 'Unauthorized'}, 401

if __name__ == '__main__':
    app.run(host='0.0.0.0')