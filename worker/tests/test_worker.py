import base64
import datetime
import json
import unittest
from .base import Base
from .mocks.worker_payload import ( valid_task_data, invalid_projectid_task_data, invalid_location_task_data , \
    invalid_queue_task_data, invalid_body_task_data )

class WorkerCase(Base):

    def test_consume_task(self):
        response = self.client().post('/consume-task', data={}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        response = self.client().post('/add-task', data=valid_task_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_queue_task(self):
        response = self.client().post('/add-task', data=invalid_queue_task_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_projectid_task(self):
        response = self.client().post('/add-task', data=invalid_projectid_task_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_location_task(self):
        response = self.client().post('/add-task', data=invalid_location_task_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_body_task(self):
        response = self.client().post('/add-task', data=invalid_body_task_data, content_type='application/json')
        self.assertEqual(response.status_code, 422)