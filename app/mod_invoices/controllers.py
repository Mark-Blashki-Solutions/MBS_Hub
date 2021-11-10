from app import db
from flask import Blueprint
import logging

# Get logger
logger = logging.getLogger()

invoices = Blueprint('simple_page', __name__)

@invoices.route('/invoices')
def list_invoices():
  logging.info("Route: '/invoices'")
  data = db.list_invoice_ids()
  return {'data': data}, 200
