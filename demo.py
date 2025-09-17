from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

logging.info('Starting the application...')

try:
    a = 2 / 0
except Exception as e:
    logging.info('Dividing by zero is not allowed.')
    raise USvisaException(e, sys)
