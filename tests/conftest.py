import pytest

from app import create_app, register_extensions, dispose
from app.helpers.document_bridge import DocumentBridge
from botocore.exceptions import ClientError

@pytest.fixture
def app():
  # create the app with common test config
  app = create_app(settings={
    "DB_FILE": "db.sqlite",
    "AWS_S3_BUCKET": "invoice-generator-test-bucket"
  })
  
  with app.app_context():
    register_extensions(app)
  
  yield app
  
  dispose(app)

@pytest.fixture
def client(app):
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
