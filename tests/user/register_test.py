import json
from app.models.user_model import User
from app import db

def test_register_user(test_client):
  """
  Test registering a new user.
  """
  # Clean up before the test
  existing_user = User.query.filter_by(email='user@example.com').first()
  if existing_user:
    db.session.delete(existing_user)
    db.session.commit()
        
  response = test_client.post('users/register', data=json.dumps({
    'email': 'user@example.com',
    'password': 'securepassword',
    'name': 'Test User'
  }), content_type='application/json')
  
  assert response.status_code == 201
  assert 'User registered successfully' in response.json['message']