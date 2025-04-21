from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('index.html', name='Pete', score=82)

@app.route('/test')
def test_route():
    return "This is a test route!"





if __name__ == '__main__':
    app.run(debug=True)
