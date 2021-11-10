class Invoice:
  line_items = None
  get_total = None
  client = None
  ID = None
  title = None
  
  def __init__(self, dict):
    vars(self).update( dict )
  
  def __init__(
    self,
    line_items,
    get_total,
    client,
    invoice_number,
    title
  ):
    self.line_items = line_items
    self.get_total = get_total
    self.client = client
    self.ID = invoice_number
    self.title = title

class Client:
  name = None
  business_name = None
  abn = None
  address_line1 = None
  address_line2 = None
  
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

class LineItem:
  quantity = None
  description = None
  total = None
  gst = None
  
  def __init__(self, dict):
    vars(self).update( dict )
  
  def __init__(self, quantity, description, total, gst="Nil"):
    self.quantity = quantity
    self.description = description
    self.total = total
    self.gst = gst
