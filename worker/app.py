"""Create a task for a given queue with an arbitrary payload."""

import os
import logging
from google.cloud import tasks_v2
from google.oauth2 import service_account
from logging.handlers import RotatingFileHandler
from flask import Flask, request
from google.protobuf import timestamp_pb2
from datetime import datetime, date, timedelta


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


credentials = service_account.Credentials.from_service_account_file(
    "serviceaccount.json")

client = tasks_v2.CloudTasksClient(credentials=credentials)


@app.route('/add-task', methods=['POST'])
def add_task():
    payload = request.json
    app.logger.info('Got Payload from add-task')
    ''' sample request
    {
	"http_method":"POST",
	"relative_uri":"/consume-task",
	"project":"api-alien",
	"location":"us-central1",
	"queue":"hello-test",
	"body":"Hello alien"
    }
    '''
    parent = client.queue_path(payload.get(
        'project', os.environ.get('PROJECTID')), payload.get('location', os.environ.get('LOCATION')),
        payload.get('queue', os.environ.get('QUEUE_NAME')))
    app.logger.info('Initialized client for app engine queue')

    task = get_app_engine_request(payload)
    app.logger.info('Created task payload for the queue')

    if payload == {}:
        return { 'message' : 'Payload cannot be empty' } , 422

    converted_payload = payload.get('body').encode()

    task['app_engine_http_request']['body'] = converted_payload
    
    app.logger.info('Started creating task for the queue')

    response, error = create_task(client, parent, task)
    if error is not None:
        app.logger.info('Error in creating the task')

        return { 'error_message': error }, 400
    app.logger.info('Task has been created and pushed in the queue')

    return {'message': 'Published task to the queue', 'response': response.name }, 200

def create_task(client, parent, task):
    response, error = ( None, ) * 2
    try: 
        response = client.create_task(parent, task)
        app.logger.info('Created task in service method')

    except Exception as e:
        app.logger.info('Error in creating Task')

        error = e.message
    return response, error

def get_app_engine_request(payload):
    task = {
        'app_engine_http_request': {
            'http_method': payload.get('http_method'),
            'relative_uri': payload.get('relative_uri')
        }
    }
    app.logger.info('App engine request object constructed')

    return task

@app.route('/consume-task', methods=['POST'])
def consume_task():
    app.logger.info('Got object from the queue to process')
    payload = request.get_data(as_text=True) or '(empty payload)'
    app.logger.info('Processing the task from the queue')
    # do something
    return {'message': 'Consumed task from the queue'}

def initialize_loggers():
    handler = RotatingFileHandler('{}.log'.format(str(date.today())), maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

if __name__ == "__main__":
    initialize_loggers()
    app.run(host='127.0.0.1', port=8020, debug=True)
