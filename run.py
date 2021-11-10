import logging
import traceback

# Get logger
logger = logging.getLogger(__name__)

from setup import *
try:
  from app import *

except Exception as e:
  logger.critical("Uncaught exception:\n%s", traceback.format_exc())
