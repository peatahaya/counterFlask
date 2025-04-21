from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def test():
    return "Hello, World!"

@app.route('/test')
def test_route():
    return "This is a test route!"

@app.route('/user/<age>')
def user(age):
    if int(age) < 21:
        return redirect('/')
    else:
        return "Welcome to the adult section!"
    
@app.route('/user1/<age>')
def user1(age):
    if int(age) < 21:
        return redirect('/')
    else:
        return "Welcome to the adult section!"
    
@app.route('/user2/<age>')
def user2(age):
    if int(age) < 21:
        return redirect(url_for('test'))
    else:
        return "Welcome to the adult section!"

if __name__ == '__main__':
    app.run(debug=True)
