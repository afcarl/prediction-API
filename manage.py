from flask_script import Manager
import unittest

from services import create_app, db
from services.model_server.models import Model, Dataset
from services.model_server.data.data_handling import create_table, parse_csv

import sys, logging

app = create_app()
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)
manager = Manager(app)


@manager.command
def recreate_db():
    """Recreate the database"""
    db.reflect()
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def test():
    tests = unittest.TestLoader().discover('services/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def seed_db():
    """Add some test samples to the database"""
    '''db.session.add(Dataset('iris',
                           'https://osdn.net/projects/sfnet_irisdss/downloads/IRIS.csv/',
                           'Classification'))
    db.session.add(Dataset('cars',
                           'https://archive.ics.uci.edu/ml/datasets/car+evaluation',
                           'Classification'))
    db.session.add(Dataset('boston_housing',
                           'https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html',
                           'Regression'))'''
    model = Model(model_name='iris', api_endpoint='iris')
    db.session.add(model)
    dataset = Dataset(dataset_name='iris', database_name='iris', url='..', task_type='Classification', target_column='Name')
    db.session.add(dataset)
    #create_table('IRIS', ('width', 'height'), ('int', 'varchar(255)'))
    db.session.commit()


@manager.command
def add_iris():
    parse_csv('iris', '/usr/src/app/services/model_server/raw_data/iris.csv')


# If main script, start the manager
if __name__ == '__main__':
    manager.run()
