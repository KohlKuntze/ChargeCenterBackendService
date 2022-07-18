import boto3
from log_utilities import log_util_factory
import config

DYNAMO_DB = 'dynamodb'
logger = log_util_factory.create_logger()


def configure_dynamo_client():

    if not config.IS_RUNNING_ON_SERVER:
        endpoint_url = config.DYNAMO_ENDPOINT_MAP[config.LOCAL_KEY]
        return boto3.client(DYNAMO_DB, endpoint_url=endpoint_url)

    return boto3.client(DYNAMO_DB)


# DYNAMO_CLIENT = configure_dynamo_client()

def get_item():
    logger.info("Getting item")
    DYNAMO_CLIENT = configure_dynamo_client()
    logger.info("DYNAMO_CLIENT configured")

    response = DYNAMO_CLIENT.get_item(
        TableName='ChargerAllocation',
        Key={
            "ChargerId": {"S": "Charger-1"}
        }
    )

    logger.info("Dynamo response: " + str(response))

    return response