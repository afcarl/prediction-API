import datetime

from services import db


class Model(db.Model):
    __tablename__ = 'models'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelname = db.Column(db.String(128), nullable=False)
    task = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    def __init__(self, modelname, task):
        self.modelname = modelname
        self.task = task
        self.created_at = datetime.datetime.utcnow()


class User:
    pass


class Dataset:
    __tablename__ = 'datasets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datasetname = db.Column(db.String(128), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    taks_type = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    def __init__(self, datasetname, url, task_type):
        self.datasetname = datasetname
        self.url = url
        self.task_type = task_type
        self.created_at = datetime.datetime.utcnow()


class Data:
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.JSON(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)


class Prediction:
    pass
