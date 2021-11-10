#!pip install tinydb
from tinydb import TinyDB, Query
from app.helpers.document_bridge import S3DocumentBridge
import app.models as models
import logging
import app

database_file_name = None
logger = None
stored_clients = None
stored_invoices = None
stored_line_items = None

def __init__():
  # Get logger
  logger = logging.getLogger()
  database_file_name = app.app.config.database_file_name
  
  db = TinyDB(database_file_name)
  stored_clients = db.table('clients')
  stored_invoices = db.table('invoices')
  stored_line_items = db.table('line_items')
  logger.info("Database initialised.")

# Wrapper decorator that keeps the DB current
def __DbUpdate(func):
  def wrapper():
    S3DocumentBridge.get(database_file_name)
    func()
    S3DocumentBridge.save(database_file_name)
  return wrapper

def get_next_invoice_number():
  raise NotImplementedError()

def add_invoice():
  raise NotImplementedError()

def list_clients():
  raise NotImplementedError()

@__DbUpdate
def add_client(client):
  stored_clients.insert(client.__dict__)

def get_client(client_name):
  Client = Query()
  # find client where name is client_name
  clients = stored_clients.search(Client.name == client_name)
  
  # return None if there were no results, otherwise return the first
  if(len(clients) == 0):
    return None
  else:
    return clients.loads(clients[0], object_hook=models.client)

def list_invoice_ids():
  return [invoice['ID'] for invoice in stored_invoices]
