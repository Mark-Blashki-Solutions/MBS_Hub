def test_404(client):
  response = client.get('/13279yfjsna98w34y7kjudsr98y734')
  assert response.status_code == 404
  
