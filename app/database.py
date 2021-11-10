from app.helpers.document_bridge import S3DocumentBridge
from app import app
import logging

# Get logger
logger = logging.getLogger()
# logger.info("Database initialised.")

# Wrapper decorator that keeps the DB current
def __DbUpdate(func):
  def wrapper():
    S3DocumentBridge.get(app.config['DB_FILE'])
    func()
    S3DocumentBridge.save(app.config['DB_FILE'])
  return wrapper

# Begin DB methods
def get_next_invoice_number():
  raise NotImplementedError()

def add_invoice():
  raise NotImplementedError()

def list_clients():
  raise NotImplementedError()

@__DbUpdate
def add_client(client):
  raise NotImplementedError()

def get_client(client_name):
  raise NotImplementedError()

def list_invoice_ids():
  raise NotImplementedError()
