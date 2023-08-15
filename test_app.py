import pytest
from app import app, db, Books, Customer, Purchase
from flask import Flask, session


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_add_to_cart(client):
    data = {
        'name': 'Book 1',
        'price': 10.0,
        'quantity': 2
    }
    response = client.post('/add_to_cart', json=data)
    assert response.status_code == 200
    assert b'Item added to cart successfully' in response.data

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'The bookish nook' in response.data

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About' in response.data

def test_contact_page(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Contact us' in response.data

def test_products_page(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert b'Products listing' in response.data

def test_category_page(client):
    response = client.get('/category')
    assert response.status_code == 200
    assert b'Category' in response.data

def test_show_cart(client):
    response = client.get('/show_cart')
    assert response.status_code == 200
    assert b'Cart' in response.data
def test_add_to_cart_invalid_request(client):
    data = {
        'invalid_key': 'Invalid Value'
    }
    response = client.post('/add_to_cart', json=data)
    assert response.status_code == 400
    assert b'Invalid request data' in response.data

def test_checkout_valid_data(client):
    response = client.post('/checkout', data={
        'firstname': 'John',
        'lastname': 'Doe',
        'email': 'john@example.com'
    })
    assert response.status_code == 200  # Redirect after successful checkout





