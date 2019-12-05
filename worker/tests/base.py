import unittest

from flask import current_app

from app import app


class Base(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)