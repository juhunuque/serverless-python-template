import json
import os
import logging
from urllib.parse import parse_qsl

# Only required for deploying
# try:
#   import unzip_requirements
# except ImportError:
#   pass


def index(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps({
            'message': 'Service: Waiting...'
        })
    }

    return response
