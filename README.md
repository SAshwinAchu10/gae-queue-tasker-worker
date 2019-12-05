# Instabot
---


### Initial Steps

$ `gcloud auth login`

#### Login from the browser and come back to the terminal

###### Set the project is using below command

$ `gcloud config set project <project-id>`

###### Goto Google cloud console and navigate to API & Services -> Credentials -> Create Credentials -> Service Account 

Download the service account json and copy paste the json content inside path `insabot/worker/serviceaccount.json`

### To run locally

$ `cd instabot`

$ `pipenv shell`

$ `pip install -r requirements.txt`

$ `python app.py`

##### Server will be running in http://127.0.0.1:8020/

Add Task to Queue - http://127.0.0.1:8020/add-task

Consume Task from Queue - http://127.0.0.1:8020/consume-task

**Note - Use ngrok to test locally**

---
### To Deploy to AppEngine

To deploy the Application to the Google App Engine use below command.

$ `gcloud app deploy app.yaml`

Add Task to Queue - https://{project-id}.appspot.com/add-task

Consume Task from Queue - https://{project-id}.appspot.com/consume-task


**Environment - Flexible**
