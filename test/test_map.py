def test_map(app, client):
    res = client.get('/map')
    html = res.data.decode()
    assert res.status_code == 200
    assert "Home" in html
    assert "Map" in html
    assert "About" in html

def test_bikeRack_location(app, client):
    res = client.get('/getlocations/bike_rack')
    assert res.status_code == 200
    data = res.text
    assert data == '["College of Science"]\n', "Bike rack list check failed"

def test_waterStation_location(app, client):
    res = client.get('/getlocations/water_station')
    assert res.status_code == 200
    data = res.text
    assert data == '["College of Science"]\n', "Test failed on obtaining water station results"