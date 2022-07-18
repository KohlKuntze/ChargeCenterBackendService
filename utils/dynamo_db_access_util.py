import boto3
from log_utilities import log_util_factory
import config

DYNAMO_DB = 'dynamodb'
logger = log_util_factory.create_logger()


def configure_dynamo_client():

    endpoint_url = config.DYNAMO_ENDPOINT_MAP[config.LOCAL_KEY]

    if config.IS_RUNNING_ON_SERVER:
        endpoint_url = config.DYNAMO_ENDPOINT_MAP[config.SERVER_KEY]

    return boto3.client(DYNAMO_DB, endpoint_url=endpoint_url)


DYNAMO_CLIENT = configure_dynamo_client()

def get_item():
    response = DYNAMO_CLIENT.get_item(
        TableName='ChargerAllocation',
        Key={
            "ChargerId": {"S": "Charger-1"}
        }
    )

    return response