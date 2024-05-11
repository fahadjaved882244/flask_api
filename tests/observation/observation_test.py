import pytest
import json
from app.models.user_model import User
from app import db

@pytest.fixture(scope="module")
def auth_token(test_client):
  # Clean up before the test
  existing_user = User.query.filter_by(email='test@example.com').first()
  if existing_user:
    db.session.delete(existing_user)
    db.session.commit()
        
  test_client.post('users/register', data=json.dumps({
    'email': 'test@example.com',
    'password': 'testpassword',
    'name': 'Test User'
  }), content_type='application/json')
  
  # Assuming you have an endpoint to authenticate users and get a token
  response = test_client.post('users/login', data=json.dumps({
      'email': 'test@example.com',
      'password': 'testpassword'
  }), content_type='application/json')
  return response.json['access_token']

def test_create_observation(test_client, auth_token: str):
  """
  Test successfully creating an observation.
  """

  observation_data = [
    {
      "date_time": "2024-04-09T12:00:00",
      "time_zone_offset": 3,
      "latitude": 40.712776,
      "longitude": -74.005974,
      "land_surface_temperature": 26.5,
      "sea_surface_temperature": 22.1,
      "humidity": 65.0,
      "wind_speed": 15.0,
      "wind_direction": 180,
      "precipitation": 5.0,
      "haze": 20.0,
      "notes": "Testing 2."
    },
  ]
  headers = {
    'Authorization': f'Bearer {auth_token}'
  }
  response = test_client.post('/observations/', headers=headers, data=json.dumps(observation_data), content_type='application/json')
  assert response.status_code == 201
  assert 'Observations stored successfully' in response.json['message']

def test_create_invalid_observation(test_client, auth_token: str):
  """
  Test error handling for creating an observation with invalid data.
  """
  invalid_observation_data = {
    'date_time': 'not-a-date',  # Invalid date format
    # Missing other mandatory fields
  }
  headers = {
    'Authorization': f'Bearer {auth_token}'
  }
  response = test_client.post('/observations/', headers=headers, data=json.dumps(invalid_observation_data), content_type='application/json')
  
  assert response.status_code == 400
  assert 'Invalid data' in response.json['error']


def test_create_observation_without_token(test_client):
  """
  Test error handling for creating an observation with invalid data.
  """
  observation_data = [
    {
      'date_time': '2024-01-01T12:00:00',
      'time_zone_offset': -5,
      'latitude': 34.05,
      'longitude': -118.25,
      'land_surface_temperature': 30,
      'sea_surface_temperature': 25,
      'humidity': 50,
      'wind_speed': 10,
      'wind_direction': 180,
      'precipitation': 5,
      'haze': 10,
      'notes': 'Sunny day',
      'user_id': 1
    }
  ]
   
  response = test_client.post('/observations/', data=json.dumps(observation_data), content_type='application/json')
  
  assert response.status_code == 401
  assert 'Missing Authorization Header' in response.json['msg']


def test_get_observations_by_user_email(test_client, auth_token: str):
  """
  Test retrieving observations for a user.
  """
  response = test_client.get('/observations/by_user_email/test@example.com', content_type='application/json')
  
  assert response.status_code == 200    
  assert type(response.json) is list
  
