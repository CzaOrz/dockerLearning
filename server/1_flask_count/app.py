from flask import Flask

app = Flask(__name__)

count = 0


@app.route('/count')
def _count():
    global count
    count += 1
    return str(count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8866)
