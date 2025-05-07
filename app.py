from flask import Flask, render_template, request
from markupsafe import escape

import sqlite3

# Create a SQLite database connection
connect = sqlite3.connect('database.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS USERS (name TEXT, \
    email TEXT, city TEXT, country TEXT, phone TEXT)'
)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/')
def show_users():
    # show the user profile for that user
    return 'This is the user route'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/dashboard/')
def render_dashboard():

    user = {
        'username': 'John Doe',
        'email': 'jd@mail.com',
        'city': 'New York',
        'country': 'USA',
    }
    notifications = [
        {'message': 'New message from Alice', 'time': '2 hours ago'},
        {'message': 'Your order has been shipped', 'time': '1 day ago'},
        {'message': 'New comment on your post', 'time': '3 days ago'},
    ]
    
    return render_template('dashboard.html', user=user, notifications=notifications)


@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        country = request.form['country']
        phone = request.form['phone']
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO USERS \
            (name,email,city,country,phone) VALUES (?,?,?,?,?)",
                           (name, email, city, country, phone))
            users.commit()
        return render_template("index.html")
    else:
        return render_template('adduser.html')

@app.route('/users')
def participants():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM USERS')

    data = cursor.fetchall()
    return render_template("users.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)
# To run the app, use the command: python app.py
