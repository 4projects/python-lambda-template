import boto3
import requests
import uuid 

import helpers

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bus-data')


def handler(event, context):
    url = 'https://api.hrtb.us/api/buses/routes'
    r = requests.get(url)
    d = r.json()
    # converts float/decimal points
    data = [ helpers.dumps(i) for i in d]
    snapshot = {
        'route': str(uuid.uuid4()),
        'data': data
    }
    table.put_item(Item=snapshot)
    return 'OK'
