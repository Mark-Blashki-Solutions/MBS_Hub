# !pip install flask_restful
# !pip install flask

from flask import Flask
from flask.wrappers import Request
from app.mod_invoices.controllers import invoices as invoices
import logging
import json

def create_app(settings_file_name):
  app = Flask(__name__)
  
  # Register blueprints
  app.register_blueprint(invoices)
  
  logger.info("Server initialized.")
  
  # Load settings from json
  app.config.from_file(settings_file_name, load=json.load)
  logger.info("Loaded settings.")
  
  return app

# Get logger
logger = logging.getLogger()

# Init flask app
logging.info("Server starting...")
app = create_app("./development.settings")

# Define universal routes
@app.route("/")
@app.route("/hello")
def hello_world():
  logger.info("Route: '/'")
  return "Hello, World!"
  
@app.errorhandler(404)
def page_not_found():
  logger.info("404!")
  return "Page Not Found!\n " + Request.url, 404

# Run app
app.run(debug=True, port=5000)

