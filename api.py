from flask import Flask, request, render_template, jsonify
from functools import wraps


TOKEN = '123'


app = Flask(__name__)


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if get_current_user_role() not in roles:
                return error_response()
            return f(*args, **kwargs)
        return wrapped
    return wrapper

def get_current_user_role():
    # pega permissao do usuario
    return 'user'

# def auth_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         try:
#             token = request.headers['Authorization']
#             if token is None:
#                 return {'state': 'fail', 'message': 'Authorization required'}, 403
#             if token != TOKEN:
#                 return {'state': 'fail', 'message': 'Invalid token'}, 403
#             return f(token=token, *args, **kwargs)
#         except Exception as e:
#             return {'state': 'fail', 'message': str(e)}, 500

#     return decorated 


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/')
@requires_roles('admin', 'user')
def user_page():
    return "You've got permission to access this page."


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>', methods=['POST'])
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #do_the_login()
        pass
    else:
        #show_the_login_form()
        pass

@app.route('/about')
def about():
    return 'about'

@app.route('/getuser')
# @auth_required
def get_current_user():
    return jsonify(
        username="Willem",
        email="willemarf@gmail.com",
        id=1
    )

if __name__ == '__main__':
    app.run()

# curl -H 'Content-Type: application/json' -X POST -d '{"username": "will"}' http://localhost:5000/user/willem
# curl -X POST -d '{"username": "will"}' http://localhost:5000/user/willem
# curl -X POST -h {'Authorization': '123'} http://localhost:5000/getuser