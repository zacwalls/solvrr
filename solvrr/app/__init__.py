from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap = Bootstrap(app)
app.config.from_object('config.BaseConfig')

from app import routes
