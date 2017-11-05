from flask_testing import TestCase
import json

from services import create_app, db


app = create_app()


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('services.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def assertResponse(self, response, status_code=None, status=None, message=None):
        data = json.loads(response.data.decode())
        if status_code is not None:
            self.assertEqual(response.status_code, status_code)
        if status is not None:
            self.assertIn(status, data['status'])
        else:
            self.assertNotIn('status', data)
        if message is not None:
            self.assertIn(message, data['message'])
        else:
            self.assertNotIn('message', data)
