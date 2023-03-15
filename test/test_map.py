def test_map(app, client):
    res = client.get('/map')
    html = res.data.decode()
    assert res.status_code == 200
    assert "Home" in html
    assert "Map" in html
    assert "About" in html
