import json
import logging
import logging.config
import sys
import traceback

from app.handlers.DefaultHandler import DefaultHandler
from app.handlers.StatConsumerHandler import StatConsumerHandler
from app.handlers.StatHandler import StatHandler
from app.utils.Logger import LOGGING_CONFIG
from app.utils.Response import build_response

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()

Handlers = {
    "get_stat": StatHandler,
    "default": DefaultHandler
}


def get_handler_type(event):
    if 'resource' in event:
        resource = event['resource'].lstrip('/').lower()
        http_method = event['httpMethod'].lstrip('/').lower()
        handler_type = Handlers["default"]
        handler_path = f"{http_method}_{resource}"
        if handler_path in Handlers:
            handler_type = Handlers['handler_path']
    else:
        handler_type = StatConsumerHandler
    return handler_type


def lambda_handler(event, context):
    logging.info('Received event: ' + json.dumps(event))
    try:
        handler_type = get_handler_type(event)
        handler = handler_type(event)
        status, response = handler.process()
        response = build_response(status, response)
        logging.info(f'Response load confirmation [{response}]')
    except Exception as e:
        logging.error(e)
        tb = sys.exc_info()[2]
        tb_info = traceback.format_tb(tb)[0]
        py_msg = "PYTHON ERRORS:\nTraceback info:\n" + tb_info + "\nError Info:\n" + str(sys.exc_info()[1])
        logging.error(py_msg)
        response = build_response(500, e.args[0])
    return response


if __name__ == '__main__':
    event = {
        "Records": [
            {
                "EventSource": "aws:sns",
                "EventVersion": "1.0",
                "EventSubscriptionArn": "arn:aws:sns:us-east-1:142347585731:test:b56a35e4-ba46-4b6c-8e92-dd90c4685278",
                "Sns": {
                    "Type": "Notification",
                    "MessageId": "f14c33f9-9eda-5df0-af9b-69e1ee8ee299",
                    "TopicArn": "arn:aws:sns:us-east-1:142347585731:test",
                    "Subject": "None",
                    "Message": "{\"isMutant\": true}",
                    "Timestamp": "2021-11-24T16:53:40.321Z",
                    "SignatureVersion": "1",
                    "Signature": "oxZ8PzZg9hrOcAqKH6DcOMQMzjn2CpGP7y8ak1FzrHivGD2fGcr9AhUZ7rXS2kI/dgG0ft8QS90acQKwbhJ7QgxbcdmaocNjqUrD4OlGteq6ZXXnbfIbpq27vq2Z5VbaB/LZAJD5lZvDfaC6dHWUf7PijdNZ2whjVqh09K5iNT9S+WF7HyHu2qKab9PkqObW2xHeC3unpNys2Z+euUz9d8ERx+ZdglWoLmYp900jV0TIay4v4PVVYVmat/hIPzEvy8P0DAw/7lz0HrpfXJTi/VafijAXwY0I6W2L2VYjig5ZmMJAJ8eB4Akc7HalSQVgWUCcX/hV69SVxlrC/u5OPg==",
                    "SigningCertUrl": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
                    "UnsubscribeUrl": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:142347585731:test:b56a35e4-ba46-4b6c-8e92-dd90c4685278",
                    "MessageAttributes": {
                    }
                }
            },
            {
                "EventSource": "aws:sns",
                "EventVersion": "1.0",
                "EventSubscriptionArn": "arn:aws:sns:us-east-1:142347585731:test:b56a35e4-ba46-4b6c-8e92-dd90c4685278",
                "Sns": {
                    "Type": "Notification",
                    "MessageId": "f14c33f9-9eda-5df0-af9b-69e1ee8ee299",
                    "TopicArn": "arn:aws:sns:us-east-1:142347585731:test",
                    "Subject": "None",
                    "Message": "{\"isMutant\": true}",
                    "Timestamp": "2021-11-24T16:53:40.321Z",
                    "SignatureVersion": "1",
                    "Signature": "oxZ8PzZg9hrOcAqKH6DcOMQMzjn2CpGP7y8ak1FzrHivGD2fGcr9AhUZ7rXS2kI/dgG0ft8QS90acQKwbhJ7QgxbcdmaocNjqUrD4OlGteq6ZXXnbfIbpq27vq2Z5VbaB/LZAJD5lZvDfaC6dHWUf7PijdNZ2whjVqh09K5iNT9S+WF7HyHu2qKab9PkqObW2xHeC3unpNys2Z+euUz9d8ERx+ZdglWoLmYp900jV0TIay4v4PVVYVmat/hIPzEvy8P0DAw/7lz0HrpfXJTi/VafijAXwY0I6W2L2VYjig5ZmMJAJ8eB4Akc7HalSQVgWUCcX/hV69SVxlrC/u5OPg==",
                    "SigningCertUrl": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
                    "UnsubscribeUrl": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:142347585731:test:b56a35e4-ba46-4b6c-8e92-dd90c4685278",
                    "MessageAttributes": {
                    }
                }
            },
        ]
    }
    # event = {
    #     "resource": "/stat",
    #     "path": "/v1/stat",
    #     "httpMethod": "GET",
    #     "queryStringParameters": None,
    #     "multiValueQueryStringParameters": None,
    #     "pathParameters": None,
    #     "stageVariables": None,
    # }
    lambda_handler(event, None)
