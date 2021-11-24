from app.StatDynamoDb.StatDynamoDb import StatDynamoDb
from app.handlers.Handler import Handler


class StatHandler(Handler):

    def __init__(self, event):
        super().__init__(event)

    def parse_parameters(self):
        super().parse_parameters()

    def __data_retrieval(self):

        stats = StatDynamoDb.get_stat()
        return 200, {
            'countHumanDna': stats['countHumanDna'],
            'countMutantDna': stats['countMutantDna'],
            'ratio': 0.0 if stats['countHumanDna'] == 0 else stats['countMutantDna'] / stats['countHumanDna']
        }

    def process(self):
        self.parse_parameters()
        if self.malformed_request:
            status_code, message = 400, {"message": "Malformed request."}
        else:
            status_code, message = self.__data_retrieval()
        return status_code, message

    def __get_ratio(self, stats):
        return .0 if stats['countHumanDna'] == 0 else stats['countMutantDna'] / stats['countHumanDna']
