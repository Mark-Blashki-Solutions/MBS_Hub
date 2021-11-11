import logging
import traceback

# Get logger
logger = logging.getLogger(__name__)

try:
  from setup import *
  from app import *
    
  # Run app
  app.run(debug=True, port=5000)



except Exception as e:
  logger.critical("Uncaught exception:\n%s", traceback.format_exc())
