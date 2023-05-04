def test_home_url(app, client):
    res = client.get('/')
    html = res.data.decode()
    assert res.status_code == 200, 'test_home_url status code failed'

def test_map_url(app, client):
    res = client.get('/map')
    html = res.data.decode()
    assert res.status_code == 200, 'test_map_url status code failed'

def test_aboutus_url(app, client):
    res = client.get('/about-us')
    html = res.data.decode()
    assert res.status_code == 200, 'test_aboutus_url failed'