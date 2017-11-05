import json

from services.tests.base import BaseTestCase
from services.model_server.models import Dataset, Data
from services import db, create_app

app = create_app()


def add_dataset(dataset_name, url, task_type):
    dataset = Dataset(dataset_name=dataset_name, url=url, task_type=task_type)
    db.session.add(dataset)
    db.session.commit()
    return dataset


def add_data(features, target, dataset_id):
    dataset = Dataset.query(Dataset.id == dataset_id).first()
    dataset.add_data(features, target)


class TestDataset(BaseTestCase):
    def test_get_datasets(self):
        """Ensure that the base /dataset route returns the right keys"""
        add_dataset('iris', 'bla', 'Classification')
        add_dataset('boston_housing', 'bla2', 'Regression')
        response = self.client.get('/dataset')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']['datasets']), 2)
        self.assertIn('bla', data['data']['datasets'][0]['url'])
        self.assertIn('bla2', data['data']['datasets'][1]['url'])
        self.assertIn('iris', data['data']['datasets'][0]['name'])
        self.assertIn('boston_housing', data['data']['datasets'][1]['name'])
        self.assertIn('Classification', data['data']['datasets'][0]['task'])
        self.assertIn('Regression', data['data']['datasets'][1]['task'])

    def test_add_dataset(self):
        """Make sure dataset gets added via POST /dataset"""
        with self.client:
            response = self.client.post(
                '/dataset',
                data=json.dumps({'name': 'Iris',
                                 'url': 'bla.com',
                                 'task': 'Classification'}),
                content_type='application/json'
            )
            self.assertResponse(response, status_code=201, status='success', message='added')

    def test_add_dataset_missing_keys(self):
        """Return fail message if not all keys are available"""
        with self.client:
            response = self.client.post(
                '/dataset',
                data=json.dumps({'name': 'Iris',
                                 'task': 'Classification'}),
                content_type='application/json'
            )
            self.assertResponse(response, status_code=400, status='fail', message='payload')

    def test_add_dataset_non_unique_name(self):
        """Return fail message if name already exists"""
        add_dataset('Iris', 'iris.com', 'Classification')
        with self.client:
            response = self.client.post(
                '/dataset',
                data=json.dumps({'name': 'Iris',
                                 'url': 'iris2.com',
                                 'task': 'Classification'}),
                content_type='application/json'
            )
            self.assertResponse(response, status_code=400, status='fail', message='already')

    def test_add_data_to_dataset_class_singular(self):
        """See that data is added to dataset"""
        dataset = add_dataset('iris3', 'iris3.com', 'Classification')
        new_features = str({'width': '2', 'height': '2'})
        new_target = str({'class': 'Versicolor-Virginica'})
        dataset.add_data(new_features, new_target)
        data = Data.query.filter((Data.target.contains('Versicolor-Virginica')) &
                                 (Data.features.contains('2'))).first()
        if not data:
            raise AssertionError('Data not found')

    def test_add_data_to_dataset_class_plural(self):
        """See that all data is added to dataset"""
        dataset = add_dataset('iris4', 'iris4.com', 'Classification')
        new_features = [str({'width': '2', 'height': '2'}),
                        str({'width': '3', 'height': '3'})]
        new_targets = [str({'class': 'Versicolor-Virginica'}),
                       str({'class': 'Orizono'})]
        dataset.add_data(new_features, new_targets)
        data = Data.query.filter(Data.dataset_id == dataset.id).all()
        if not data:
            raise AssertionError('Data not found')
        else:
            self.assertEqual(len(data), 2)