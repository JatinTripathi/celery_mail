from flask import send_from_directory
from flask import render_template

from gateway import app
from gateway.models import Mails


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


def logging(err):
    print err