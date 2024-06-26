from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.observation_service import ObservationService
from app.services.user_service import UserService
from app.schemas.observation_schema import ObservationSchema, GetObservationSchema

observation_blueprint = Blueprint('observations', __name__, url_prefix='/observations')

@observation_blueprint.route('/', methods=['POST'])
@jwt_required()
def create_observations():
    # Validate and deserialize input
    schema = ObservationSchema(many=True)
    try:
        observations_data = schema.load(request.json)
    except Exception:
        return jsonify({"error": "Invalid data"}), 400
    
    results = []
    user_email = get_jwt_identity()
    user = UserService.get_user_by_email(user_email)
    
    if not user:
        return jsonify({"error": "User not found"}), 404

    try:
        for data in observations_data:
            observation = ObservationService.create_observation(
                user_id=user.id,
                date_time=data['date_time'],
                time_zone_offset=data['time_zone_offset'],
                latitude=data['latitude'],
                longitude=data['longitude'],
                land_surface_temperature=data['land_surface_temperature'],
                sea_surface_temperature=data['sea_surface_temperature'],
                humidity=data['humidity'],
                wind_speed=data['wind_speed'],
                wind_direction=data['wind_direction'],
                precipitation=data['precipitation'],
                haze=data['haze'],
                notes=data['notes']
            )
            results.append(observation)
        
        return jsonify({'message': 'Observations stored successfully', 'ids': [obs.id for obs in results]}), 201

    except Exception as e:
        print(f"Unexpected error during store observations: {e}")
        return jsonify({'message': 'Store observations failed due to an unexpected error'}), 500


@observation_blueprint.route('/<int:observation_id>', methods=['GET'])
def get_observation_by_id(observation_id):
    observation = ObservationService.get_observation(observation_id)
    if observation:
        result = GetObservationSchema().dump(observation)
        return jsonify(result), 200
    else:
        return jsonify({"error": "Observation not found"}), 404

@observation_blueprint.route('/by_user_email/<string:user_email>', methods=['GET'])
def get_observations_by_user_email(user_email):
    list_of_observation = ObservationService.get_observations_by_user_email(user_email)
    if list_of_observation is not None:
        result = GetObservationSchema(many=True).dump(list_of_observation)
        return jsonify(result), 200
    else:
        return jsonify({"error": "User not found"}), 404


@observation_blueprint.route('/<int:observation_id>', methods=['PUT'])
@jwt_required()
def update_observation(observation_id):
    user_email = get_jwt_identity()
    user = UserService.get_user_by_email(user_email)
    
    if not user:
        return jsonify({"error": "User not found"}), 404


    observation = ObservationService.get_observations_by_user_id_and_observation_id(user_id=user.id, observation_id=observation_id)
    if observation is None:
         return jsonify({"error": "Observation not found"}), 404
    
    # Check if the observation's date_time is within the current quarter
    current_quarter_start = get_current_quarter_start()
    if observation.date_time < current_quarter_start:
        return jsonify({"error": "Can not amend records prior to the current quarter."}), 404
    
    # Validate and deserialize input
    schema = ObservationSchema()
    data = schema.load(request.json)
    
    updated_observation = ObservationService.update_observation(
        observation_id,
        date_time = data.get('date_time'),
        time_zone_offset = data.get('time_zone_offset'),
        latitude = data.get('latitude'),
        longitude = data.get('longitude'),
        land_surface_temperature = data.get('land_surface_temperature'),
        sea_surface_temperature = data.get('sea_surface_temperature'),
        humidity = data.get('humidity'),
        wind_speed = data.get('wind_speed'),
        wind_direction = data.get('wind_direction'),
        precipitation = data.get('precipitation'),
        haze = data.get('haze'),
        notes = data.get('notes')
    )
    if updated_observation:
        result = GetObservationSchema().dump(updated_observation)
        return jsonify(result), 200
    else:
        return jsonify({"error": "Unexpected error occur"}), 404


@observation_blueprint.route('/<int:observation_id>', methods=['DELETE'])
@jwt_required()
def delete_observation(observation_id):
    user_email = get_jwt_identity()
    user = UserService.get_user_by_email(user_email)
    
    if not user:
        return jsonify({"error": "User not found"}), 404


    observation = ObservationService.get_observations_by_user_id_and_observation_id(user_id=user.id, observation_id=observation_id)
    if observation is None:
         return jsonify({"error": "Observation not found"}), 404
    
    # Check if the observation's date_time is within the current quarter
    current_quarter_start = get_current_quarter_start()
    if observation.date_time < current_quarter_start:
        return jsonify({"error": "Can not amend records prior to the current quarter."}), 404
    
    result = ObservationService.delete_observation(observation_id)
    if result:
        return jsonify({"success": "Observation deleted"}), 200
    return jsonify({"error": "Observation not found"}), 404


# Helpers
from datetime import datetime

def get_current_quarter_start():
    current_date = datetime.now()
    current_quarter = (current_date.month - 1) // 3 + 1
    start_month = 3 * (current_quarter - 1) + 1
    return datetime(current_date.year, start_month, 1)