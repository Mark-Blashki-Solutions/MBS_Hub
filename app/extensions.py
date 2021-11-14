from flask.blueprints import Blueprint
from flask_sqlalchemy import SQLAlchemy
from app.helpers.document_bridge import DocumentBridge, MockDocumentBridge

db = SQLAlchemy()
document_bridge = MockDocumentBridge()
# document_bridge = DocumentBridge()
