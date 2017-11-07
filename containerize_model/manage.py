from flask_script import Manager

from app import app

manager = Manager(app)


# If main script, start the manager
if __name__ == '__main__':
    manager.run()