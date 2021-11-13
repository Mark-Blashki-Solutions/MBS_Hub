from app.extensions import document_bridge
from app.models import InvoiceSchema, ClientSchema, LineItemSchema
from flask import current_app

# Initialise Schemas
invoice_schema = InvoiceSchema()
client_schema = ClientSchema()
line_item_schema = LineItemSchema()

invoices_schema = InvoiceSchema(many=True)
clients_schema = ClientSchema(many=True)
line_items_schema = LineItemSchema(many=True)

# Wrapper decorator that keeps the DB current
def db_update(app):
  def decorator(func):
    def wrapper():
      document_bridge.get(app.config['DB_FILE'])
      func()
      document_bridge.save(app.config['DB_FILE'])
    return wrapper
  return decorator
