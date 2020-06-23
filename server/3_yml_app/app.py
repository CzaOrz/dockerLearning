from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/test')


@app.route('/test')
def test():
    return "hello world"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8866)
