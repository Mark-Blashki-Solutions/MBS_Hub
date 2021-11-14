from app.extensions import db
from dataclasses import dataclass
import json

# Models
# TODO: add type checking and valdation

@dataclass
class Client(db.Model):
  name : str
  business_name : str
  abn : str
  address_line1 : str
  address_line2 : str
  
  _tablename__ = "clients"
  name = db.Column(db.String(120), primary_key=True)
  business_name = db.Column(db.String(120), unique=True)
  abn = db.Column(db.String(15), unique=True)
  address_line1 = db.Column(db.String(200))
  address_line2 = db.Column(db.String(200))
  
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

@dataclass
class Invoice(db.Model):
  id : str
  client_name : str
  client : Client
  title : str
  line_items : list
  is_paid : bool
  is_deleted : bool
  
  _tablename__ = "invoices"
  id = db.Column(db.String(36), primary_key=True)
  client_name = db.Column(db.String(120), db.ForeignKey('client.name'))
  client = db.relationship('Client', backref=db.backref("invoices", lazy=True))
  title = db.Column(db.String(120), nullable=False)
  line_items = db.relationship('LineItem', backref=db.backref('invoices', lazy=True))
  is_paid = db.Column(db.Boolean, default=False)
  is_deleted = db.Column(db.Boolean, default=False)
  
  
  @classmethod
  def from_params(
    self,
    client=None,
    ID=None,
    title=None,
    line_items=None
  ):
    self.id = ID
    self.line_items = line_items
    self.client = client
    self.title = title

@dataclass
class LineItem(db.Model):
  id : int
  invoice_id : str
  quantity : int
  description : str
  total : float
  gst : float
  
  _tablename__ = "line_items"
  id = db.Column(db.Integer, primary_key=True)
  invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))
  quantity = db.Column(db.Float)
  description = db.Column(db.String(300))
  total = db.Column(db.Float)
  gst = db.Column(db.Float)
  
  @classmethod
  def from_params(self, quantity=None, description=None, total=None, gst=0, invoice_id=None):
    self.quantity = quantity
    self.description = description
    self.total = total
    self.invoice_id = invoice_id
    self.gst = gst
