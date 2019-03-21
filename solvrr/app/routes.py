import random
import os
from flask import Flask, render_template, url_for, flash, request

from app import app


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        with open(os.path.abspath(os.path.dirname(__file__)) + '/solutions.txt', 'r') as f:
            lines = f.readlines()
            flash(random.choice(lines))
    return render_template('index.html')
