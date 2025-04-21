from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return "Hello, World!"

@app.route('/test')
def test_route():
    return "This is a test route!"

@app.route('/user', defaults={'username': 'guest', 'age': 25})
@app.route('/user/<username>/<age>')
def user_profile(username, age):
    return f"User profile for {username}, age: {age}"



if __name__ == '__main__':
    app.run(debug=True)
