from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask_restful import Api
import pymysql

app = Flask(__name__)
api = Api(app)
CORS(app)

def get_data_sql(code):
    db_connect = pymysql.connect(
        host='flask-backend.ckxv07dhtiyg.ap-northeast-1.rds.amazonaws.com',
        user='admin',
        passwd='12345678',
        port=3306,)

    cursor = db_connect.cursor()

    # sql = '''CREATE TABLE ecdsa (address STRING,ecdsa_code STRING);'''
    sql = "use flaskbackend"
    cursor.execute(sql)
    #'''SELECT * FROM ecdsa'''
    sql = code
    cursor.execute(sql)

    data = cursor.fetchall()

    cursor.connection.commit()

    return data

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/testing", methods=['GET'])
def testing_function():
    x = get_data_sql('SELECT * from ecdsa')
    return jsonify({"message" : x}),200



if __name__ == '__main__':
    app.run(debug=False)