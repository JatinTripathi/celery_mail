import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

config = 'gateway.config.{}'.format(os.environ['APP_ENV'])
app.config.from_object(config)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import gateway.views