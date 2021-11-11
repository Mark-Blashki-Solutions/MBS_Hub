import tests.conftest

def test_create_app(client):
  result = client.get('/invoices/')
  # assert "h" in "hello"
  assert b"[]" in result.data
