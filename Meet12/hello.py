# from flask import Flask
#
# app = Flask(__name__)
# from flask import render_template
#
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
# @app.route('/post/<int:post_id>')
# def show_id(post_id):
#     return f'Hello, world #{post_id}!'
#
# @app.route('/user/<username>')
# def hello_user(username):
#     return f'User {username} connected'
#
# @app.route('/path/<path:subpath>')
# def all_path(subpath):
#     return f'You are here: {subpath}'
#
#
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
def valid_login(name,password):
    return name==password
@app.route('/logged/<name>')
def log_the_user_in (name):
    return f" Hello, you are an authorized user {name} "
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run()