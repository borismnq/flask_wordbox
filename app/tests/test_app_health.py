def test_app_health(app):
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
