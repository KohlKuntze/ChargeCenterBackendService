from flask import Flask, request, json
# from logging_utils import logging_configurator
#
#
# logger = logging_configurator.configure_logger()

from logging.handlers import TimedRotatingFileHandler
from logging import Formatter
import logging

# get named logger
logger = logging.getLogger(__name__)

# create handler
handler = TimedRotatingFileHandler(filename='application.log', when='D', interval=1, backupCount=90, encoding='utf-8', delay=False)

# create formatter and add to handler
formatter = Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handler to named logger
logger.addHandler(handler)

# set the logging level
logger.setLevel(logging.INFO)

# --------------------------------------

# log something
logger.info("test")


def create_app():
    application = Flask(__name__)

    # flask_env = os.getenv("FLASK_ENV")

    return application


application = create_app()


@application.route('/')
def index():
    return "Test"


@application.route('/test_json', methods=['POST'])
def asdf():
    return "Test2"


@application.route('/post_json', methods=['POST'])
def process_json():
    logger.info("received request to /post_json")
    data = json.loads(request.data)
    return data


if __name__ == '__main__':
    application.debug = True
    application.run()
