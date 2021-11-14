from app.database import *


def test_db_update(app):
  @db_update(app)
  def test_func():
    pass
  
  test_func()
