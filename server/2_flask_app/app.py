#!/usr/bin/env python
# coding: utf-8
from flask import Flask, redirect

app = Flask(__name__)
count = 0


@app.route('/')
def index():
    return redirect('/hello')


@app.route('/hello')
@app.route('/hello/<string:name>')
def test(name="world"):
    return f"hello {name}"


@app.route('/count')
def _count():
    global count
    count += 1
    return str(count)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8866)
