import pytest

from app import create_app, register_extensions, dispose

@pytest.fixture
def app():
  # create the app with common test config
  app = create_app("testing.settings")
  
  with app.app_context():
    register_extensions(app)
  
  yield app
  
  dispose(app)

@pytest.fixture
def client(app):
  return app.test_client()
