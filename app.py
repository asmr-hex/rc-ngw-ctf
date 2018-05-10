from flask import Flask, render_template, request
import sqlite3 as sql


app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(username)
        print(password)

        # authenticate the user and stuff...
        # conn = sql.connect('cops.db')
        # cursor = conn.cursor()
        # cursor.execute('SELECT * FROM users WHERE username="robocop"')

        # all_rows = cursor.fetchall()

        # print(all_rows)

        return 'hiiii'
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
