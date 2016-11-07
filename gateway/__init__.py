import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery


app = Flask(__name__)

config = 'gateway.configurations.{}'.format(os.environ['APP_ENV'])
app.config.from_object(config)


##################### Celery Setup ########################
def make_celery(app):
    celery = Celery(app.import_name, 
                    backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
###########################################################


celery = make_celery(app)
db = SQLAlchemy(app)

import gateway.views