from app.models import *

def test_invoice_from_params():
  
  line_items = [LineItem().from_params(1, "description", 1, 0),
                LineItem().from_params(1, "description", 1, 0)]
  invoice = Invoice()
  invoice.from_params(line_items, "client", "invoice_id", "title")
  
  assert invoice.client_name == "client"
  assert invoice.title == "title"
  assert invoice.id == "invoice_id"
  assert invoice.line_items == line_items
  
def test_line_item_from_params():
  line_item = LineItem()
  line_item.from_params(1, "description", 100, "invoice_id", 0.5)
  assert line_item.description == "description"
  assert line_item.gst == 0.5
  assert line_item.quantity == 1
  assert line_item.total == 100
  assert line_item.invoice_id == "invoice_id"

def test_client_from_params():
  client = Client()
  client.from_params("name", "business_name", "abn", "address_line1", "address_line2")
  assert client.name == "name"
  assert client.business_name == "business_name"
  assert client.abn == "abn"
  assert client.address_line1 == "address_line1"
  assert client.address_line2 == "address_line2"

def test_invoice_dict_constructor():
  line_items = [LineItem().from_params(1, "description", 1, 0),
                LineItem().from_params(1, "description", 1, 0)]
  
  invoice = Invoice({
    "client_name": "client_name",
    "title": "title",
    "id": "invoice_id",
    "line_items": line_items
  })
  
  assert invoice.client_name == "client_name"
  assert invoice.title == "title"
  assert invoice.id == "invoice_id"
  assert invoice.line_items == line_items
  
def test_line_item_dict_constructor():
  line_item = LineItem({
    "description": "description",
    "gst": 0.5,
    "quantity": 1,
    "total": 100,
    "invoice_id": "invoice_id"
  })
  assert line_item.description == "description"
  assert line_item.gst == 0.5
  assert line_item.quantity == 1
  assert line_item.total == 100
  assert line_item.invoice_id == "invoice_id"

def test_client_dict_constructor():
  client = Client({
    "name": "name",
    "business_name": "business_name",
    "abn": "abn",
    "address_line1": "address_line1",
    "address_line2": "address_line2"
  })
  assert client.name == "name"
  assert client.business_name == "business_name"
  assert client.abn == "abn"
  assert client.address_line1 == "address_line1"
  assert client.address_line2 == "address_line2"
