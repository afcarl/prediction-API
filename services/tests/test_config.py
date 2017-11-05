import unittest

from flask import current_app
from flask_testing import TestCase

from services import create_app

app = create_app()

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('services.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'secret_key')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] ==
                        'postgres://postgres:postgres@postgres-db:5432/prediction_dev')


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('services.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'secret_key')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] ==
                        'postgres://postgres:postgres@postgres-db:5432/prediction_test')


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('services.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'secret_key')
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])



if __name__ == '__main__':
    unittest.main()