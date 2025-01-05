import pytest
import sys
import os
import json



src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from app import app

# @pytest.fixture
# def client():
#     # Setup: Initialize Flask test client
#     with app.test_client() as client:
#         # Setup the app context (needed for database operations)
#         with app.app_context():
#             db.create_all()  # Create all tables for testing
#         yield client
#         # Teardown: Clean up after the test
#         with app.app_context():
#             db.drop_all()  

@pytest.fixture
def client():
    with app.app_context(): 
        app.config.update({
            "TESTING": True
        })
        yield app.test_client()