import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'My Blog' in rv.data

def test_new_post_page(client):
    rv = client.get('/new')
    assert rv.status_code == 200
    assert b'New Post' in rv.data

def test_create_post(client):
    rv = client.post('/new', data=dict(
        title='Test Title',
        content='Test Content'
    ), follow_redirects=True)
    assert rv.status_code == 200
    assert b'Test Title' in rv.data
    assert b'Test Content' in rv.data
