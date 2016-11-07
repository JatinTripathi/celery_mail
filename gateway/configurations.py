import os


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/mails'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@db/mails'

    # CELERY_BROKER_URL = 'redis://redis'
    # CELERY_RESULT_BACKEND = 'redis://redis'
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    # CELERY_QUEUES = (
    #     Queue('default', Exchange('default'), routing_key='default'),
    #     Queue('for_task_A', Exchange('for_task_A'), routing_key='for_task_A'),
    #     Queue('for_task_B', Exchange('for_task_B'), routing_key='for_task_B'),
    # )
    # CELERY_ROUTES = {
    #     'my_taskA': {'queue': 'for_task_A', 'routing_key': 'for_task_A'},
    #     'my_taskB': {'queue': 'for_task_B', 'routing_key': 'for_task_B'},
    # }
    CELERY_IGNORE_RESULT = True
    CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'Asia/Kolkata'
    


class Production(Config):
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False


class Testing(Config):
    TESTING = True
    DEBUG = False
    DEVELOPMENT = False


class Staging(Config):
    TESTING = False
    DEBUG = True
    DEVELOPMENT = True
    CSRF_ENABLED = False


class Development(Config):
    TESTING = False
    DEBUG = True
    DEVELOPMENT = True
    CSRF_ENABLED = False
