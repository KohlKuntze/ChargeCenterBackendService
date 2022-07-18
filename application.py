from flask import Flask
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

application.register_blueprint(charger_information_blueprint, url_prefix="/information")


# Register Routes

if __name__ == '__main__':
    application.debug = True
    application.run()

