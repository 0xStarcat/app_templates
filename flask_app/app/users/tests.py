import unittest
from app import create_app
from tests import TestConfig, drop_test_db
import setup


class UsersCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        setup.setup_db()

    def tearDown(self):
        drop_test_db()
        self.app_context.pop()

    def test_case(self):
        self.assertEqual(1, 1)
