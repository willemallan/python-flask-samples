from flask import Flask, request, render_template, jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

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
# curl -X POST http://localhost:5000/user/willem