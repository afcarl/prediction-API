from flask_script import Manager

from services import create_app, db


app = create_app()
manager = Manager(app)


@manager.command
def recreate_db():
    """Recreate the database"""
    db.drop_all()
    db.create_all()
    db.session.commit()


# If main script, start the manager
if __name__ == '__main__':
    manager.run()
