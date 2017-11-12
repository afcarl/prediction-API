import datetime

from services import db

# from sqlalchemy.dialects.postgresql.json import JSONB


class CustomModel:
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class Model(db.Model, CustomModel):
    __tablename__ = 'model'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model_name = db.Column(db.String(128), nullable=False)
    api_endpoint = db.Column(db.String(32), nullable=False)

    def __init__(self, model_name, api_endpoint):
        self.model_name = model_name
        self.api_endpoint = api_endpoint


class Dataset(db.Model, CustomModel):
    __tablename__ = 'dataset'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dataset_name = db.Column(db.String(128), nullable=False)
    database_name = db.Column(db.String(128), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    task_type = db.Column(db.String(100), nullable=False)
    target_column = db.Column(db.String(100), nullable=False)

    def __init__(self, dataset_name, database_name, url, task_type, target_column, filename=None):
        self.dataset_name = dataset_name
        self.database_name = database_name
        self.url = url
        self.task_type = task_type
        self.target_column = target_column
        if filename is not None:
            pass

    #def add_data(self, features, target):
    #    if not isinstance(features, list):
    #        features = [features]
    #        target = [target]
    #    for feature_sample, target_sample in zip(features, target):
    #        sample = Data(feature_sample, target_sample)
    #        self.data.append(sample)
    #    db.session.commit()

'''
class Data(db.Model, CustomModel):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    features = db.Column(db.String(10000), nullable=False)
    target = db.Column(db.String(10000))
    dataset_id = db.Column(db.Integer, db.ForeignKey('dataset.id'), nullable=False)

    def __init__(self, features, target):
        self.features = features
        self.target = target
'''