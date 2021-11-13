from app.database import *


def test_db_update(app):
  # mocker.patch('app.extensions.document_bridge.get')
  # mocker.patch('app.extensions.document_bridge.save')
  # TODO: Mock document_bridge
  @db_update(app)
  def test_func():
    pass
  
  test_func()
