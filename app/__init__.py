# !pip install flask_restful
# !pip install flask

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import logging
import os
import json

def create_app(settings_file_name):
  app = Flask(__name__)
  base_dir = os.path.dirname(os.path.dirname(__file__))
  
  app.config["DB_FILE"] = "db.sqlite"
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, )
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  logger.info("Server initialized.")
  
  db = SQLAlchemy(app)
  logger.info("DB initialized.")
  
  marshmallow = Marshmallow(app)
  logger.info("Marshmallow initialized.")
  
  # Load settings from json
  app.config.from_file(settings_file_name, load=json.load)
  logger.info("Loaded settings.")
  
  return app, db, marshmallow

# Get logger
logger = logging.getLogger()

# Init flask app
logging.info("Server starting...")
app, db, marshmallow = create_app("./development.settings")

# Define universal routes
@app.route("/")
@app.route("/hello")
def hello_world():
  logger.info("Route: '/'")
  return "Hello, World!"
  
@app.errorhandler(404)
def page_not_found():
  logger.info("404!")
  return "Page Not Found!", 404

# Run app
app.run(debug=True, port=5000)

