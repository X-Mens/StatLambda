import logging


class Handler:

    def __init__(self, event):
        self.event = event
        self.resource = event['resource'].lstrip('/').lower()
        self.http_method = event['httpMethod'].lstrip('/').lower()
        self.malformed_request = False
        self.logger = logging.getLogger(__name__)

    def __data_retrieval(self):
        pass

    def parse_parameters(self):
        pass

    def process(self):
        pass
