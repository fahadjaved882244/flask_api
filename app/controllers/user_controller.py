from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.services.jwt_service import JWTService
from sqlalchemy.exc import SQLAlchemyError

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/register', methods=['POST'])
def register_user():
  data = request.get_json()
  email = data.get('email')
  password = data.get('password')
  name = data.get('name')
  
  try:
    existing_user = UserService.get_user_by_email(email)
    if existing_user:
      return jsonify({'message': 'Email already registered'}), 409
    else:  
      UserService.create_user(email, password, name)
      return jsonify({'message': 'User registered successfully'}), 201
  
  except SQLAlchemyError as e:
    # Log the error as appropriate
    print(f"Database error during registration: {e}")
    return jsonify({'message': 'Registration failed due to a server error'}), 500
  
  except Exception as e:
    # Catch any other unexpected errors
    print(f"Unexpected error during registration: {e}")
    return jsonify({'message': 'Registration failed due to an unexpected error'}), 500


@user_blueprint.route('/login', methods=['POST'])
def login_user():
  data = request.get_json()
  email = data.get('email')
  password = data.get('password')

  try:
    if UserService.authenticate_user(email, password):
      # Assuming you have a method to generate JWT tokens
      access_token, refresh_token = JWTService.generate_tokens(email)
      return jsonify({
          'message': 'Login successful',
          'access_token': access_token,
          'refresh_token': refresh_token
      }), 200
    else:
      return jsonify({'message': 'Invalid email or password'}), 401
    
  except SQLAlchemyError as e:
    # Log the error as appropriate
    print(f"Database error during login: {e}")
    return jsonify({'message': 'Login failed due to a server error'}), 500
  
  except Exception as e:
    # Catch any other unexpected errors
    print(f"Unexpected error during login: {e}")
    return jsonify({'message': 'Login failed due to an unexpected error'}), 500