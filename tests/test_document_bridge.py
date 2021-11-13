from tempfile import NamedTemporaryFile
import os
import pytest

from app.helpers.document_bridge import DocumentBridge

def test_constructor(app):
  bridge = DocumentBridge()
  bridge.init_app(app)
  
def test_save(mock_document_bridge):
  with NamedTemporaryFile(delete=False) as tmp:
    assert mock_document_bridge.save(tmp.name)
    tmp.close()

@pytest.mark.slow
def test_get(document_bridge):
  with open("tmp.txt", "w+") as tmp:
    tmp.writelines("test");
    tmp.close()
    
  document_bridge.save("tmp.txt")
  
  os.remove("tmp.txt")
  
  document_bridge.get("tmp.txt")
  
  assert os.path.isfile("tmp.txt") 
  
  with open("tmp.txt", "r") as tmp:
    assert tmp.read() == "test"

def test_faulty_s3_upload(faulty_document_bridge):
  assert not faulty_document_bridge.save("tmp.txt")
