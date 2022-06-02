import requests

API_URL = "localhost:8000"

def test_root():
    r = requests.get("http://localhost:8000{}".format("/"))
    assert r.status_code==200

    assert "status" in r.json()

def test_test():
    r = requests.get("http://localhost:8000{}".format("/test"))
    assert r.status_code==200
    assert "test"==r.json()

def test_post():
    r = requests.post("http://localhost:8000{}".format("/post_test"))
    assert r.status_code==200
    assert 25==r.json()

def test_health():
    r = requests.get("http://localhost:8000{}".format("/health"))
    assert r.status_code==200
    assert "health" in r.json()


