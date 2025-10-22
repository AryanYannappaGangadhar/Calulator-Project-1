import logging
import os

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.DEBUG

log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logging.basicConfig(
    filename=os.path.join(log_directory, "app.log"),
    level=LOG_LEVEL,
    format=LOG_FORMAT,
)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)

def log_debug(message):
    logging.debug(message)