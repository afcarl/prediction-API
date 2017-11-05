import datetime

from services import db

from sqlalchemy.dialects.postgresql.json import JSONB


class CustomModel:
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class Model(db.Model, CustomModel):
    __tablename__ = 'models'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelname = db.Column(db.String(128), nullable=False)
    task = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, modelname, task):
        self.super()
        self.modelname = modelname
        self.task = task


class Dataset(db.Model, CustomModel):
    __tablename__ = 'dataset'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dataset_name = db.Column(db.String(128), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    task_type = db.Column(db.String(100), nullable=False)
    data = db.relationship('Data', backref='dataset')

    def __init__(self, dataset_name, url, task_type):
        self.dataset_name = dataset_name
        self.url = url
        self.task_type = task_type

    def add_data(self, features, target):
        if not isinstance(features, list):
            features = [features]
            target = [target]
        for feature_sample, target_sample in zip(features, target):
            sample = Data(feature_sample, target_sample)
            self.data.append(sample)
        db.session.commit()


class Data(db.Model, CustomModel):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    features = db.Column(db.String(10000), nullable=False)
    target = db.Column(db.String(10000))
    dataset_id = db.Column(db.Integer, db.ForeignKey('dataset.id'), nullable=False)

    def __init__(self, features, target):
        self.features = features
        self.target = target
