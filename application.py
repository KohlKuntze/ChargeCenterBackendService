from flask import Flask, request, json
from log_utilities import log_util_factory
from information.charger_information import charger_information_blueprint


logger = log_util_factory.create_logger()


logger.info("Initiating Flask App")


def create_app():
    logger.info("Creating App")
    application = Flask(__name__)

    # flask_env = os.getenv("FLASK_ENV")

    return application


application = create_app()


logger.info("Registering Route '/' with application")
@application.route('/')
def index():
    logger.info("Got request for for route /")
    return "Test"


logger.info("Registering Route '/test_json' with application")
@application.route('/test_json', methods=['POST'])
def asdf():
    return "Test2"


logger.info("Registering Route '/post_json' with application")
@application.route('/post_json', methods=['POST'])
def process_json():
    logger.info("received request to /post_json")
    data = json.loads(request.data)
    return data


# Register Routes
application.register_blueprint(charger_information_blueprint, url_prefix="/information")

if __name__ == '__main__':
    application.debug = True
    application.run()
