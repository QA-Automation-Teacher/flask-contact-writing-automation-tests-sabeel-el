# import pytest
# from app import app, db
# from models import Contacts



# '''
# @pytest.fixture
# def client():
#     #with app.test_client() as client:
#         #yield client
#     with app.app_context(): 
#         app.config.update({
#             "TESTING": True
#         })
#         yield app.test_client()
# '''

# # @pytest.fixture
# # def client():
# #     # Setup: Initialize Flask test client
# #     with app.test_client() as client:
# #         # Setup the app context (needed for database operations)
# #         with app.app_context():
# #             db.create_all()  # Create all tables for testing
# #         yield client
# #         # Teardown: Clean up after the test
# #         with app.app_context():
# #             db.drop_all()  

# @pytest.fixture
# def contact(client):
#     """Fixture to add a contact for testing"""
#     contact = Contacts(name='Jane', surname='Doe', email='jane.doe@example.com', phone='9876543210')
#     db.session.add(contact)
#     db.session.commit()
#     return contact


# def test_get_request(client):
#     response = client.get('/new_contact')
#     assert response.status_code == 200

# def test_get_all(client,contact):
    
#     response = client.get('/api/contacts')
#     assert response.status_code == 200

# def test_get_type(client,contact):
    
#     response = client.get('/api/contacts')
#     assert isinstance(response.get_json(), list) 


# def test_delete_contact(client,contact):
    
#     response = client.get(f'/contacts/delete/{contact.id}')
#     assert response.status_code == 302
from migrations import create_fake_contacts
from app import app
from models import db


BASE_URL = "http://localhost:5000"

def setup_module(module):
    with app.app_context():
        db.drop_all()
        db.create_all
        create_fake_contacts()


def teardown_module(module):
    with app.app_context():
        db.session.remove()
        db.drop_all()


def test_get_contacts(client):
    response = client.get(BASE_URL + "/api/contacts/17")
    assert response.status_code == 200
    assert isinstance(response.get_json(), dict)

def test_get_request(client):
    response = client.get('/new_contact')
    assert response.status_code == 200

def test_get_all(client):
    response = client.get(BASE_URL + "/api/contacts")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)