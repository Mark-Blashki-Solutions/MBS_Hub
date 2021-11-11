from app.extensions import document_bridge
from app.models import InvoiceSchema, ClientSchema, LineItemSchema

# Initialise Schemas
invoice_schema = InvoiceSchema()
client_schema = ClientSchema()
line_item_schema = LineItemSchema()

invoices_schema = InvoiceSchema(many=True)
clients_schema = ClientSchema(many=True)
line_items_schema = LineItemSchema(many=True)

# Wrapper decorator that keeps the DB current
def DbUpdate(func):
  def wrapper():
    document_bridge.get()
    func()
    document_bridge.save()
  return wrapper
