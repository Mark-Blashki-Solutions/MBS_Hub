import pytest

from app import create_app, register_extensions, dispose
from app.helpers.document_bridge import DocumentBridge
from botocore.exceptions import ClientError
from app.models import *

@pytest.fixture
def app():
  # create the app with common test config
  app = create_app(settings={
    "DB_FILE": "db.sqlite",
    "AWS_S3_BUCKET": "invoice-generator-test-bucket"
  })
  
  with app.app_context():
    register_extensions(app)
  
  # Fill in test db data
  db.drop_all()
  db.create_all()
  client = Client(name="name",
                  business_name="business_name",
                  abn="abn",
                  address_line1="address_line1",
                  address_line2="address_line2")
  db.session.add(client)
  
  invoice = Invoice(client=client,
                    id="invoice_id_1",
                    title="title")
  line_item_1 = LineItem(quantity=5,
                  description="description2",
                  total=50,
                  gst=5)
  line_item_2 = LineItem(quantity=1,
                  description="description",
                  total=100,
                  gst=0)
  
  invoice.line_items.append(line_item_1)
  invoice.line_items.append(line_item_2)
  db.session.add(invoice)
  db.session.commit()
  
  yield app
  
  dispose(app)

@pytest.fixture
def client(mocker, app):
  mocker.patch('app.extensions.document_bridge.get')
  mocker.patch('app.extensions.document_bridge.save', True)
  return app.test_client()

@pytest.fixture
def document_bridge(app):
  bridge = DocumentBridge()
  bridge.init_app(app)
  return bridge

@pytest.fixture
def mock_document_bridge(mocker, app):
  bridge = DocumentBridge()
  bridge.init_app(app)
  mocker.patch("boto3.s3.inject.upload_file", return_value=None)
  mocker.patch("boto3.s3.inject.download_file", return_value=None)
  return bridge

@pytest.fixture
def faulty_document_bridge(mocker, document_bridge):
  mocker.patch('boto3.s3.inject.upload_file', side_effect=ClientError(error_response={
    'Error': {
      'Code': 'TEST',
      'Message': 'Throttling',
    }
  }, operation_name="Put"))
  
  return document_bridge
