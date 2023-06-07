# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/post/<int:post_id>')
# def show_id(post_id):
#     return f'Hello, world #{post_id*2}!'
#
# @app.route('/user/<username>')
# def hello_user(username):
#     return f'User {username} connected'
#
# @app.route('/path/<path:subpath>')
# def all_path(subpath):
#     return f'You are here: {subpath}'
#
# if __name__ == '__main__':
#     app.run()

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)