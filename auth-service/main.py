from flask import Flask
from flask import request
from flaskext.mysql import MySQL
import os
import sys
import jwt
import time

app = Flask(__name__)

mysql = MySQL()
# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "password"
app.config["MYSQL_DATABASE_DB"] = "AUTHSERVICE"
app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_SERVICE_PORT"))
mysql.init_app(app)

@app.route("/jwt-token")
def jwt_issuer():
    username = request.args.get('username')
    password = request.args.get('password')
    # match the username and password against sources
    sql = "SELECT * FROM users WHERE user_name = %s"

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, username)
        result_set = cursor.fetchall()
        for row in result_set:
            if row[3] == password:
                cursor.close()
                conn.close()
                now = int(time.time())
                return jwt.encode({'application': "jwt-issuer"}, os.environ["JWT_SECRET"], algorithm="HS256", headers = {"iss": username, "iat": now, "exp": now + 300})
        return {'status': 'Unauthorized'}, 401
    except Exception as exception:
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