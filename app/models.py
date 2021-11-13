from app.extensions import db, marshmallow

# Models
# TODO: add type checking and valdation


class Invoice(db.Model):
  id = db.Column(db.String(36), primary_key=True)
  line_items = db.relationship('LineItem', backref="invoice", lazy=True)
  client_name = db.Column(db.Integer, db.ForeignKey('client.name'))
  title = db.Column(db.String(120), nullable=False)
  
  def __init__(self, dict:dict=None):
    if(dict != None): vars(self).update(dict)
  
  @classmethod
  def from_params(
    self,
    line_items=None,
    client_name=None,
    ID=None,
    title=None
  ):
    self.id = ID
    self.line_items = line_items
    self.client_name = client_name
    self.title = title
    return self

class Client(db.Model):
  name = db.Column(db.String(120), primary_key=True)
  business_name = db.Column(db.String(120), unique=True)
  abn = db.Column(db.String(15), unique=True)
  address_line1 = db.Column(db.String(200))
  address_line2 = db.Column(db.String(200))
  invoices = db.relationship('Invoice', backref="client", lazy=True)
  
  def __init__(self, dict:dict=None):
    if(dict != None): vars(self).update(dict)
  
  @classmethod
  def from_params(
    self,
    name=None,
    business_name=None,
    abn=None,
    address_line1=None,
    address_line2=None
  ):
    self.name = name
    self.business_name = business_name
    self.abn = abn
    self.address_line1 = address_line1
    self.address_line2 = address_line2
    return self

class LineItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))
  quantity = db.Column(db.Float)
  description = db.Column(db.String(300))
  total = db.Column(db.Float)
  gst = db.Column(db.Float)
  
  def __init__(self, dict:dict=None):
    if(dict != None): vars(self).update(dict)
  
  @classmethod
  def from_params(self, quantity=None, description=None, total=None, invoice_id=None, gst=0):
    self.quantity = quantity
    self.description = description
    self.total = total
    self.invoice_id = invoice_id
    self.gst = gst
    return self

# Schemas
class InvoiceSchema(marshmallow.Schema):
  class Meta:
    fields = ("id",
              "line_items",
              "client_name",
              "title")

class ClientSchema(marshmallow.Schema):
  class Meta:
    fields = ("name",
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
