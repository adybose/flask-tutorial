from flask import Flask, render_template
from markupsafe import escape


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
    return render_template('dashboard.html', name="dashboard")



if __name__ == '__main__':
    app.run(debug=True)
# To run the app, use the command: python app.py
