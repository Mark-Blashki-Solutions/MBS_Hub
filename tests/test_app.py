import tests.conftest
from app import create_app, dispose, register_extensions
from tempfile import NamedTemporaryFile
import os
import pytest

def test_create_app_no_settings():
  # Ensure that testing is set correctly
  with pytest.raises(TypeError):
    assert create_app()

def test_create_app_settings_files():
  # ensure that settings load from development file
  assert create_app(settings_file="development.settings")
  
  # ensure that settings load from testing file
  assert create_app(settings_file="testing.settings")
  
  # ensure that settings load from file
  with NamedTemporaryFile(delete=False) as tmp:
    tmp.write('{"DB_FILE": "test_file","AWS_S3_BUCKET": "InvoiceGeneratorDB"}'.encode('utf8'))    
    tmp.close()
    assert create_app(settings_file=tmp.name).config["DB_FILE"] == "test_file"
    
    os.unlink(tmp.name)

def test_create_app_settings_dict():
  # ensure that settings load from development file
  assert create_app(settings={"DB_FILE": "test_file","AWS_S3_BUCKET": "InvoiceGeneratorDB"})

def test_register_extensions():
  app = create_app(settings_file="testing.settings")
  register_extensions(app)

def test_validate_settings():
  with pytest.raises(ValueError):
    create_app(settings={"AWS_S3_BUCKET": "InvoiceGeneratorDB"})

def test_dispose():
  app = create_app(settings_file="testing.settings")
  register_extensions(app)
  dispose(app)
