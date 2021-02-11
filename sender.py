import requests
import time
import os
from requests.auth import HTTPBasicAuth
import json

organization = os.environ['SC_ORG']
token = os.environ['SC_TOKEN']
project = os.environ['PROJECT_KEY']

x = requests.post(f'https://dev.sc-dev.io/api/projects/create?organization={organization}&name={project}&project={project}',
               auth=HTTPBasicAuth(token, ''))
print(x.text)

files = {'report': open(f'/Users/tom/Downloads/{project}.zip','rb')}
x = requests.post(f'https://dev.sc-dev.io/api/ce/submit?projectKey={project}&organization={organization}',
                    auth=HTTPBasicAuth(token, ''),
                    files=files)
taskId = json.loads(x.text)['taskId']

status = "PENDING"
while status != 'FAILED':
    status = json.loads(requests.get(f'https://dev.sc-dev.io/api/ce/task?id={taskId}',
               auth=HTTPBasicAuth(token, '')).text)['task']['status']
    print(status)
    time.sleep(1)

x = requests.post(f'https://dev.sc-dev.io/api/projects/delete?project={project}',
               auth=HTTPBasicAuth(token, ''))






