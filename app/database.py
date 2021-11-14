from app.extensions import document_bridge
from flask import current_app

# Wrapper decorator that keeps the DB current
def db_update(app):
  def decorator(func):
    def wrapper():
      document_bridge.get(app.config['DB_FILE'])
      func()
      document_bridge.save(app.config['DB_FILE'])
    return wrapper
  return decorator
