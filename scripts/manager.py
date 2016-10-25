from flask_script import Manager

from goals import app

manager = Manager(app)


@manager.command
def init():
    pass

@manager.command
def migrate():
    pass

if __name__ == "__main__":
    manager.run()