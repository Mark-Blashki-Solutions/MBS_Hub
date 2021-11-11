from flask.blueprints import Blueprint
from flask import current_app, request, jsonify
from app.database import *
from app.models import Invoice
import logging

# Get logger
logger = logging.getLogger()

# Initialise blueprint
invoices = Blueprint('invoices', __name__)

@invoices.route('/', methods=['GET'])
def get_invoices():
  invoices = Invoice.query.all()
  return jsonify({'data': invoices_schema.dump(invoices)}), 200

# @DbUpdate
# @invoices.route('/', methods=['POST'])
# def add_invoice(invoice: Invoice):
#   request.json["id"]
#   request.json["line_items"]
#   request.json["client_id"]
#   request.json["title"]
#   return jsonify({'data': invoices_schema.dump(invoices)}), 200
