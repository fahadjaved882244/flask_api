import json
from app.models.user_model import User
from app import db

def test_login_user(test_client):
  """
  Intergation test for register and logging in a user.
  """
  # Clean up before the test
  existing_user = User.query.filter_by(email='user@example.com').first()
  if existing_user:
    db.session.delete(existing_user)
    db.session.commit()
    
  # First, create a user to log in with
  response = test_client.post('users/register', data=json.dumps({
    'email': 'user@example.com',
    'password': 'securepassword',
    'name': 'Test User'
  }), content_type='application/json')
  assert response.status_code == 201

  # Now, test login
  login_response = test_client.post('users/login', data=json.dumps({
    'email': 'user@example.com',
    'password': 'securepassword'
  }), content_type='application/json')
  
  assert login_response.status_code == 200
  assert 'access_token' in login_response.json
  assert 'refresh_token' in login_response.json
