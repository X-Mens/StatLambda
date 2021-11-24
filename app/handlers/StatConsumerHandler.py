import json

from app.persistence.StatDynamoDb import StatDynamoDb


class StatConsumerHandler:

    def __init__(self, event):
        self.event = event

    def parse_parameters(self):

        self.messages = list()
        for record in self.event['Records']:
            sns_message = record['Sns']['Message']
            if isinstance(sns_message, str):
                self.messages.append(json.loads(sns_message))
            else:
                self.messages.append(sns_message)

    def __data_retrieval(self):

        for message in self.messages:
            if message['isMutant']:
                StatDynamoDb.increase_counter_dna_mutant()
            else:
                StatDynamoDb.increase_counter_dna_human()

    def process(self):
        self.parse_parameters()
        self.__data_retrieval()
        return 200, {}
