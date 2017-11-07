from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import numpy as np
import pickle
import os

from base_model import BaseModel

class Model(BaseModel):
    def __init__(self):
        self.columns = ('Sepal length', 'Sepal width', 'Petal length', 'Petal width')
        self.targets = {0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'}
        self.model = None

    def predict(self, data):
        if isinstance(data['Sepal length'], list):
            data = np.array([data[c] for c in self.columns]).T
        else:
            data = np.array([[data[c] for c in self.columns]])
        prediction = self.model.predict(data)
        return_dict = {'prediction': [self.targets[p] for p in prediction]}
        return return_dict

    def fit(self):
        iris_data = load_iris()
        X = iris_data.data
        y = iris_data.target
        self.model = RandomForestClassifier()
        self.model.fit(X, y)

    def save(self):
        with open('model.pkl', 'wb') as model_pkl:
            model_pkl.write(pickle.dumps(self.model))

    def load(self):
        if os.path.exists('model.pkl'):
            with open('model.pkl', 'rb') as model_pkl:
                self.model = pickle.loads(model_pkl.read())
        else:
            self.fit()
