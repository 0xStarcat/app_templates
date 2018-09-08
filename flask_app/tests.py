import os
import unittest
from config import Config
from app.users.models import User


class TestConfig(Config):
    TESTING = True
    FLASK_ENV = 'testing'
    MONGO_URI = os.environ.get('TEST_DATABASE_URL')
    ELASTICSEARCH_URL = os.environ.get('TEST_ELASTICSEARCH_URL')


def drop_test_db():
    pass


from app.users.tests import UsersCase

if __name__ == '__main__':
    unittest.main(verbosity=2)
