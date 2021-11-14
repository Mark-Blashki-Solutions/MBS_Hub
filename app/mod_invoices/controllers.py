from operator import inv
from flask.blueprints import Blueprint
from flask import request, jsonify, make_response
from app.database import *
from app.extensions import db
from app.models import Invoice, Client, LineItem
import logging
import json
import app.database

# Get logger
logger = logging.getLogger()

# Initialise blueprint
invoices = Blueprint('invoices', __name__)

@invoices.route('/', methods=['GET'])
def get_invoices():
  invoices = db.session.query(Invoice).join(LineItem).join(Client).all()
  
  return make_response(jsonify(invoices), 200)


@invoices.route('/<invoice_id>/', methods=['GET'])
def get_invoice_by_id(invoice_id):
  invoice = db.session.query(
    Invoice
  ).filter(
    Invoice.id == invoice_id
  ).join(LineItem).join(Client).first()
  
  return make_response(jsonify(invoice), 200)

@db_update
@invoices.route('/', methods=['POST'])
def add_invoice():
  body = request.get_json()
  invoice_id = body["id"] # TODO: replace with db call
  line_items = []
  
  for line_item in body["line_items"]:
    line_items.append(LineItem(quantity=line_item["quantity"],
                          description=line_item["description"],
                          total=line_item["total"],
                          gst=line_item["gst"]))
  client_name = body["client_name"] # TODO: validat client nname
  title = body["title"]
  
  # client = Client.query.filter_by(name=client_name).first()
  
  # if(client is None):
  #   return jsonify({'errors': [f"client '{client_name}' not found. Try adding a client first"]}), 400
  
  invoice = Invoice(line_items=line_items,
                    client_name=client_name,
                    id=invoice_id,
                    title=title)
  
  try:
    db.session.add(invoice)
    db.session.commit()
  except:
    logger.info(f"Error adding invoice {invoice_id}")
    return make_response(f"Error adding invoice {invoice_id}", 400)
  
  logger.debug("Invoice: ")
  logger.debug(jsonify(invoice))
  
  return make_response(jsonify(invoice), 200)
