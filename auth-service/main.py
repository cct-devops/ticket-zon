from flask import Flask
from flask import request
import os
import sys
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
            return jwt.encode({'application': "jwt-issuer"}, os.environ["JWT_SECRET"], algorithm="HS256", headers = {"iss": username, "iat": now, "exp": now + 300})
            
    return {'status': 'Unauthorized'}, 401

@app.route("/jwt-verify")
def jwt_verify():
    token = request.args.get('token')
    try:
        return jwt.decode(token, os.environ["JWT_SECRET"], algorithms=["HS256"])
    except:
        return {'status': 'Unauthorized'}, 401
    

if __name__ == '__main__':
    if not "JWT_SECRET" in os.environ:
        sys.exit("JWT_SECRET not set")
    app.run(host='0.0.0.0')