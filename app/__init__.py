from flask import Flask
import logging
import os
import json
from app.mod_invoices.controllers import invoices as invoice_controller
from app.extensions import db, marshmallow, document_bridge

# Get logger
logger = logging.getLogger()

# Define universal routes
def page_not_found(e):
  logger.info("404!")
  return "<h1>Page Not Found!</h1>", 404

def create_app(settings_file_name):
  app = Flask(__name__)
  
  # Load settings from json
  app.config.from_file(settings_file_name, load=json.load)
  logger.debug("Loaded settings.")
  
  base_dir = os.path.dirname(os.path.dirname(__file__))
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, app.config["DB_FILE"])
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  
  logger.debug("Server initialized.")
  
  return app

def register_extensions(app):
  # Register routes
  app.register_blueprint(invoice_controller, url_prefix='/invoices')
  app.register_error_handler(404, page_not_found)
  
  db.init_app(app)
  with app.app_context():
    db.create_all()
  db.app = app
  logger.debug("DB initialized.")
  
  marshmallow.init_app(app)
  logger.debug("Marshmallow initialized.")
  
  document_bridge.init_app(app)
  logger.debug("Document Bridge initialized.")
  
  logger.debug("URL Map:\n" + str(app.url_map))
  
  logger.debug("Extensions registered.")

def dispose(app):
  db.session.close()
  db.engine.dispose()

# Init flask app
logging.debug("Server starting...")
app = create_app("./development.settings")
register_extensions(app)
logger.info("App Loaded.")

# Retrieve database from S3
document_bridge.get(app.config['DB_FILE'])
logger.debug("DB recieved from S3")
