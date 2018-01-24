import boto3
import requests
import uuid 
from time import time
from datetime import datetime

import helpers

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bus-time-series')


def handler(event, context):
    url = 'https://api.hrtb.us/api/buses/routes'
    r = requests.get(url)
    d = r.json()
    # converts float/decimal points
    data = [ helpers.dumps(i) for i in d]
    snapshot = {
        'date': str(datetime.now()),
        'time': int(time()),
        'data': data
    }
    table.put_item(Item=snapshot)
    return 'OK'
