from boto3.dynamodb.types import TypeDeserializer
from decimal import Decimal
from datetime import datetime

import uuid
import json

# https://github.com/boto/boto3/issues/665#issuecomment-286130739
def decode_object_hook(dct):
    for key, val in dct.items():
        if isinstance(val, float):
            dct[key] = Decimal(str(val))
        if isinstance(val, list):
            val = [Decimal(str(i)) for i in val]
            dct[key] = [Decimal(str(i)) for i in val]
        try:
            dct[key] = TypeSerializer().serialize(val)
        except:
            dct[key] = val
    return dct


def json_serial(val):
    if isinstance(val, datetime):
        serial = val.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return serial
    elif isinstance(val, set):
        serial = list(val)
        return serial
    elif isinstance(val, uuid.UUID):
        serial = str(val.hex)
        return serial

def dumps(dct, *args, **kwargs):
    kwargs['object_hook'] = decode_object_hook
    return json.loads(json.dumps(dct, default=json_serial), *args, **kwargs)