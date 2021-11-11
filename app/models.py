from app.extensions import db, marshmallow

# Models

class Invoice(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  line_items = db.relationship('LineItem', backref="invoice", lazy=True)
  client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
  title = db.Column(db.String(120), nullable=False)
  
  def __init__(self, dict):
    vars(self).update(dict)
  
  def __init__(
    self,
    line_items,
    client,
    ID,
    title
  ):
    self.ID = ID
    self.line_items = line_items
    self.client = client
    self.title = title

class Client(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), unique=True)
  business_name = db.Column(db.String(120), unique=True)
  abn = db.Column(db.String(15), unique=True)
  address_line1 = db.Column(db.String(200))
  address_line2 = db.Column(db.String(200))
  invoices = db.relationship('Invoice', backref="client", lazy=True)
  
  def __init__(self, dict):
    vars(self).update( dict )
  
  def __init__(
    self,
    name,
    business_name,
    abn,
    address_line1,
    address_line2
  ):
    self.name = name
    self.business_name = business_name
    self.abn = abn
    self.address_line1 = address_line1
    self.address_line2 = address_line2

class LineItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))
  quantity = db.Column(db.Float)
  description = db.Column(db.String(300))
  total = db.Column(db.Float)
  gst = db.Column(db.Float)
  
  def __init__(self, dict):
    vars(self).update( dict )
  
  def __init__(self, quantity, description, total, gst=0):
    self.quantity = quantity
    self.description = description
    self.total = total
    self.gst = gst

# Schemas
class InvoiceSchema(marshmallow.Schema):
  class Meta:
    fields = ("id",
              "line_items",
              "client_id",
              "title")

class ClientSchema(marshmallow.Schema):
  class Meta:
    fields = ("id",
              "name",
              "business_name",
              "abn",
              "address_line1",
              "address_line2",
              "invoices")

class LineItemSchema(marshmallow.Schema):
  class Meta:
    fields = ("id",
              "invoice_id",
              "quantity",
              "description",
              "total",
              "gst")
