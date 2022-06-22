from logging.handlers import TimedRotatingFileHandler
from logging import Formatter
import logging


LOG_FILENAME = 'application.log'
LOG_FILE_BACKUP_COUNT = 90
LOG_FILE_ENCODING = 'utf-8'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def create_logger():

    # get named logger
    logger = logging.getLogger(__name__)

    # create handler
    handler = TimedRotatingFileHandler(filename=LOG_FILENAME,
                                       when='D',
                                       interval=1,
                                       backupCount=LOG_FILE_BACKUP_COUNT,
                                       encoding=LOG_FILE_ENCODING,
                                       delay=False)

    # create formatter and add to handler
    formatter = Formatter(fmt=LOG_FORMAT)
    handler.setFormatter(formatter)

    # add the handler to named logger
    logger.addHandler(handler)

    # set the logging level
    logger.setLevel(logging.INFO)

    return logger
