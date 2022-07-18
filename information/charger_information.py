from flask import Blueprint, request, json
from log_utilities import log_util_factory
from utils import dynamo_db_access_util
import os, sys
import random

logger = log_util_factory.create_logger()


current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)


charger_information_blueprint = Blueprint('charger_information', __name__)

CHARGER_NAME_KEY = 'charger_name'
PORT_INFO_KEY = 'port_info'


LOWER_BOUND = -0.05
UPPER_BOUND = 0.05


def compute_sum(new_allocations_dict: dict):
    sum = 0

    for current_port_key in new_allocations_dict.keys():
        sum = sum + new_allocations_dict[current_port_key]

    return sum


def reduce_dict_sum_to_zero(new_allocations_dict: dict):
    sum = compute_sum(new_allocations_dict)

    for current_port_key in new_allocations_dict.keys():
        new_allocations_dict[current_port_key] = new_allocations_dict[current_port_key] / sum


def generate_new_allocation(current_allocation: float):
    return_val = current_allocation + round(random.uniform(LOWER_BOUND, UPPER_BOUND), 2)

    if return_val < 0.0 or return_val > 1.0:
        return_val = 0.5

    return return_val


def generate_random_allocations(port_info_dict: dict):
    new_allocations_dict = dict()

    for current_port_key in port_info_dict.keys():
        new_allocations_dict[current_port_key] = generate_new_allocation(port_info_dict[current_port_key])

    reduce_dict_sum_to_zero(new_allocations_dict)

    return new_allocations_dict



# @charger_information_blueprint.route('/get_charge_allocation', methods=["POST", "GET"])
# def get_charge_allocation():
#     logger.info("received request to /get_charge_allocation")
#
#     charger_name = request.args.get(CHARGER_NAME_KEY)
#     logger.info("Got request for charger {}".format(charger_name))
#
#     port_info_dict = json.loads(request.args.get(PORT_INFO_KEY))
#     logger.info(port_info_dict)
#
#     new_charge_allocation_dict = generate_random_allocations(port_info_dict)
#
#     charger_response = {
#         CHARGER_NAME_KEY: charger_name,
#         PORT_INFO_KEY: new_charge_allocation_dict
#     }
#
#     return charger_response


@charger_information_blueprint.route('/get_charger_allocation', methods=["GET"])
def get_charge_allocation():
    logger.info("received request to /get_charger_allocation")

    return dynamo_db_access_util.get_item()
