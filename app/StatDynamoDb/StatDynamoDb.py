import logging

from boto3 import resource

DYNAMO_TABLE = 'stat'  # getenv("DYNAMO_TABLE")
AGGREGATION_KEY = 'aggregation'  # getenv("AGGREGATION_KEY")

dynamodb = resource('dynamodb')
stat_table = dynamodb.Table(DYNAMO_TABLE)


class StatDynamoDb:

    @staticmethod
    def increase_counter_dna_mutant():

        StatDynamoDb.increase_value_by_one('countMutantDna')

    @staticmethod
    def increase_counter_dna_human():

        StatDynamoDb.increase_value_by_one('countHumanDna')

    @staticmethod
    def increase_value_by_one(row):
        response = stat_table.update_item(
            Key={
                'aggregation': AGGREGATION_KEY
            },
            UpdateExpression=f"set {row} = if_not_exists({row}, :default_value) + :val",
            ExpressionAttributeValues={
                ':default_value': 0,
                ':val': 1
            },
            ReturnValues="UPDATED_NEW"
        )

    @staticmethod
    def get_stat():

        try:
            response = stat_table.get_item(Key={'aggregation': AGGREGATION_KEY})
        except Exception as e:
            logging.error(e.response['Error']['Message'])
            response['Item'] = {'countHumanDna': 0, 'countMutantDna': 0}
        else:
            print()
            return {
                'countHumanDna': int(response['Item']['countHumanDna']) if 'Item' in response else 0,
                'countMutantDna': int(response['Item']['countMutantDna']) if 'Item' in response else 0
            }
