from flask.blueprints import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.helpers.document_bridge import DocumentBridge, MockDocumentBridge

db = SQLAlchemy()
marshmallow = Marshmallow()
document_bridge = MockDocumentBridge()
# document_bridge = DocumentBridge()
