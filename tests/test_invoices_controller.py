def test_get_all_invoices(client):
  # TODO: Mock DB
  response = client.get('/invoices/')
  assert response.status_code == 200
  
def test_redirect_on_no_trailing_slash(client):
  # TODO: Mock DB
  response = client.get('/invoices')
  assert response.status_code == 308
