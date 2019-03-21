import random
import os
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, url_for, flash, request

app = Flask(__name__)
Bootstrap = Bootstrap(app)
app.config.from_object('config.BaseConfig')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        with open(os.path.abspath(os.path.dirname(__file__)) + '/solutions.txt', 'r') as f:
            lines = f.readlines()
            flash(random.choice(lines))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='192.168.10.42', port=5000)
