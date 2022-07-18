from flask import Blueprint
from log_utilities import log_util_factory
from utils import dynamo_db_access_util
import os, sys


logger = log_util_factory.create_logger()


current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)


charger_information_blueprint = Blueprint('charger_information', __name__)

CHARGER_NAME_KEY = 'charger_name'
PORT_INFO_KEY = 'port_info'


@charger_information_blueprint.route('/get_charger_allocation', methods=["GET"])
def get_charge_allocation():
    logger.info("received request to /get_charger_allocation")

    return dynamo_db_access_util.get_item()
