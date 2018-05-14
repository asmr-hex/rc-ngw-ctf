from flask import Flask, render_template, request
import sqlite3 as sql
import requests


key = 'key-61bcaa9e01ecd55dc9826333f9ea7276'
base_email_url = 'graveyard.rip'


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

        # authenticate the user and stuff...
        conn = sql.connect('cops.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username="%s"' % username)
        all_rows = cursor.fetchall()

        # somehow leak the users data
        if len(all_rows) == 0:
            # return error message
            return render_template(
                'login.html', error="no such user %s" % username)
        else:
            # since usrnames must be unique, just take the first one from list
            username = all_rows[0][0]
            db_password = all_rows[0][1]
            # does the password checkout?
            if db_password != password:
                # throw error
                return render_template(
                'login.html', error='incorrect password for user %s' % username)

        return render_template(
            'account.html', username=username)
    elif request.method == 'GET':
        return render_template(
            'login.html')


@app.route('/forgot', methods=['GET', 'POST'])
def password_reset():
    if request.method == 'POST':
        username = request.form['username']

        # authenticate the user and stuff...
        conn = sql.connect('cops.db')
        cursor = conn.cursor()
        cursor.execute('SELECT password, CASE WHEN username == "%s" THEN email ELSE "invalid" END FROM users' % username)
        all_rows = cursor.fetchall()

        # get the email
        email = all_rows[0][1]
        if email == "invalid":
            return render_template(
                'reset.html', error= "no such user %s" % username)

        # get password for this valid email
        password = all_rows[0][0]

        request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(base_email_url)
        requests.post(request_url, auth=('api', key), data={
            'from': 'admin@lolpd.gov',
            'to': email,
            'subject': 'ATTN OFFICER: PLS FIND YOUR SECRET PASSWORD ENCLOSED!',
            'text': 'Next time don\'t forget your password...\n\n\npassword: %s' % password,
        })

        return render_template(
                'reset.html', success='email sent to %s!' % email)
    elif request.method == 'GET':
        return render_template(
            'reset.html')


@app.route('/profile/<name>')
def profile(name):
    return render_template(
        'profile.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=44203)
