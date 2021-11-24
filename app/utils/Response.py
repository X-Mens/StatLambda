import json
import logging


def build_response(resp_code, response):
    """Builds a response object
    Parameters:
        response: Dictionary
        resp_code: Int
    Returns:
        response: Dictionary"""

    resp_code = str(resp_code) if not isinstance(resp_code, str) else resp_code

    response = {
        'statusCode': resp_code,
        'body': json.dumps(response),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Authorization,Content-Type,X-Api-Key',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST',
            'Access-Control-Allow-Credentials': True
        }
    }

    return response
