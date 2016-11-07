from flask import send_from_directory
from flask import render_template
from flask import jsonify
from flask import request

from gateway import app
from gateway.models import Mails
from gateway.tasks import *


@app.route('/api/home/static/<path:path>')
def send_static(path):
    try: return send_from_directory('static', path)

    except Exception ,e:
        logging(e)


@app.route("/api/home/")
def home():
    try: return render_template('home.html')

    except Exception ,e:
        logging(e)


@app.route('/add/')
def add_route():
    first_num = int(request.args.get('x'))
    second_num = int(request.args.get('y'))
    print type(first_num), second_num

    add.delay(first_num, second_num)

    return jsonify(result='Success')


def logging(err):
    print err