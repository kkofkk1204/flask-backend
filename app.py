from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask_restful import Api
from sqlalchemy import create_engine
from sqlalchemy import text

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/testing", methods=['GET'])
def testing_function():
    DATABASE_URL  = 'mysql://admin:12345678@flask-backend.ckxv07dhtiyg.ap-northeast-1.rds.amazonaws.com:3306/'
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        connection.execute("use flaskbackend")
        query = text("SELECT * FROM ecdsa")
        blog_posts = connection.execute(query)
        x = []
        for post in blog_posts:
            x.append(post)
        print(x)
    return jsonify({"message" : str(x)}),200



if __name__ == '__main__':
    app.run(debug=False)