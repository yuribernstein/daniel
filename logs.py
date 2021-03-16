import logging
import os

if os.getenv('LOG_FILE_LOCATION'):
    log_file_location = os.getenv('LOG_FILE_LOCATION')
else:
    log_file_location = "cert_log.json"

logging.basicConfig(
    filename=log_file_location,
    format='%(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)

file_handler = logging.FileHandler(filename=log_file_location, mode='w')

logger = logging.getLogger(__file__)

logger.addHandler(file_handler)
