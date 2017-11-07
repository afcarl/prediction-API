from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import numpy as np
import json

from base_model import BaseModel

class Model(BaseModel):
    def __init__(self):
        self.columns = ('Sepal length', 'Sepal width', 'Petal length', 'Petal width')
        self.targets = {0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'}
        self.model = None

    def predict(self, data):
        data = json.loads(data)
        if isinstance(data['Sepal length'], list):
            data = np.array([data[c] for c in self.columns]).T
        else:
            data = np.array([[data[c] for c in self.columns]])
        prediction = self.model.predict(data)
        return_json = {'prediction': [self.targets[p] for p in prediction]}
        return json.loads(return_json)

    def fit(self):
        iris_data = load_iris()
        X = iris_data.data
        y = iris_data.target
        self.model = RandomForestClassifier()
        self.model.fit(X, y)

    def save(self):
        pass

    def load(self):
        pass


iris = Iris()
print(iris.columns)
iris.fit()
print(iris.y)

single_predict = json.dumps({'Sepal length': 2.,
                             'Sepal width' : 3.,
                             'Petal length': 4.,
                             'Petal width': 5.})

iris.predict(single_predict)

plural_predict = json.dumps({'Sepal length': [2., 3.],
                             'Sepal width' : [3., 4.],
                             'Petal length': [4., 3.],
                             'Petal width':  [5., 3.]})

iris.predict(plural_predict)