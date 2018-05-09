from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3:///users.sqlite3'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template(
        'index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # authenticate the user and stuff...
        print(username)
        print(password)

        return ''
    elif request.method == 'GET':
        return render_template(
            'login.html')


@app.route('/profile/<name>')
def profile(name):
    return render_template(
        'profile.html', name=name)


@app.route("/products")
def products(name):
    return render_template(
        'test.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
