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

def create_app(settings_file=None, settings=None):
  # Initialise flask app
  app = Flask(__name__)
  
  # Load settings from settings parameters
  if(settings_file != None):
    app.config.from_file(settings_file, json.load)
  elif(settings != None):
    app.config.update(settings)
  else:
    raise TypeError("You must specify 'settings' or 'settings_file' parameter")
  
  # Validate settings
  if validate_config(app) == False: raise ValueError("Invalid settings configuration")
  logger.debug("Settings loaded and validated.")
  
  # Finish populating misc. settings
  base_dir = os.path.dirname(os.path.dirname(__file__))
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, app.config["DB_FILE"])
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  
  logger.debug("Server initialized.")
  
  return app

def validate_config(app):
  required_settings = ["DB_FILE", "AWS_S3_BUCKET"]
  
  ok = True
  for setting in required_settings:
    if setting not in app.config:
      logger.error(f"Invalid settings configuration: missing settting '{setting}'")
      ok = False
  return ok

def register_extensions(app):
  # Register routes
  app.register_blueprint(invoice_controller, url_prefix='/invoices')
  app.register_error_handler(404, page_not_found)
  
  # Link db and initialise
  db.init_app(app)
  with app.app_context():
    db.create_all()
  db.app = app
  logger.debug("DB initialized.")
  
  # Link Marshmallow
  marshmallow.init_app(app)
  logger.debug("Marshmallow initialized.")
  
  # Link document_bridge
  document_bridge.init_app(app)
  logger.debug("Document Bridge initialized.")
  
  logger.debug("URL Map:\n" + str(app.url_map))
  
  logger.debug("Extensions registered.")

def dispose(app):
  # Dispose of DB
  db.session.close()
  db.engine.dispose()

# Init flask app
logging.debug("Server starting...")
app = create_app(settings={
  "DB_FILE": "db.sqlite",
  "AWS_S3_BUCKET": "InvoiceGeneratorDB"
})
register_extensions(app)
logger.info("App Loaded.")

# Retrieve database from S3
document_bridge.get(app.config['DB_FILE'])
logger.debug("DB recieved from S3")
