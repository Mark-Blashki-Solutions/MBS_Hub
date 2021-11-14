import json

def test_get_all_invoices(client):
  # TODO: Mock DB
  response = client.get('/invoices/')
  assert response.status_code == 200

def test_get_invoice_by_id(client):
  # TODO: Mock DB
  response = client.get('/invoices/invoice_id_1/')
  assert response.status_code == 200


def test_redirect_on_no_trailing_slash(client):
  # TODO: Mock DB
  response = client.get('/invoices')
  assert response.status_code == 308

def test_add_invoice(client):
  data = """
    {
      "title": "title",
      "id": "invoice_id",
      "line_items": [
        {
          "quantity": 1,
          "description": "description",
          "total": 100,
          "gst": 0
        }
      ],
      "client_name": "name"
    }
  """
  
  response = client.post("/invoices/", data=data,
    headers={
      "content-type": 'application/json',
      "accept": "application/json",
      "mimetype": "application/json"})
  
  assert response.status_code == 200
  assert response.content_type == 'application/json'
  body = json.loads(response.get_data(as_text=True))
  assert body['title'] == 'title'
  assert body['id'] == 'invoice_id'
  assert body['line_items'][0]["quantity"] == 1
  assert body['line_items'][0]["description"] == "description"
  assert body['line_items'][0]["total"] == 100
  assert body['line_items'][0]["gst"] == 0
  assert body['client']['name'] == 'name'

def test_add_duplicate_invoice(client):
  data = """
    {
      "title": "title",
      "id": "invoice_id",
      "line_items": [],
      "client_name": "name"
    }
  """
  
  headers = {
      "content-type": 'application/json',
      "accept": "application/json",
      "mimetype": "application/json"}
  
  response = client.post("/invoices/", data=data,
    headers=headers)
  
  assert response.status_code == 200
  
  response = client.post("/invoices/", data=data,
    headers=headers)
  
  assert response.status_code == 400
