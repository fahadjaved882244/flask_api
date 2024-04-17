from flask import Blueprint, request, jsonify
from app.services.observation_service import ObservationService
from app.schemas.observation_schema import ObservationSchema

observation_blueprint = Blueprint('observations', __name__, url_prefix='/observations')

@observation_blueprint.route('/', methods=['POST'])
def create_observation():
   # Validate and deserialize input
    schema = ObservationSchema()
    data = schema.load(request.json)
    
    date_time = data.get('date_time')
    time_zone_offset = data.get('time_zone_offset')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    land_surface_temperature = data.get('land_surface_temperature')
    sea_surface_temperature = data.get('sea_surface_temperature')
    humidity = data.get('humidity')
    wind_speed = data.get('wind_speed')
    wind_direction = data.get('wind_direction')
    precipitation = data.get('precipitation')
    haze = data.get('haze')
    notes = data.get('notes')
    user_id = data.get('user_id')

    try:
        observation = ObservationService.create_observation(
            date_time=date_time,
            time_zone_offset=time_zone_offset,
            latitude=latitude,
            longitude=longitude,
            land_surface_temperature=land_surface_temperature,
            sea_surface_temperature=sea_surface_temperature,
            humidity=humidity,
            wind_speed=wind_speed,
            wind_direction=wind_direction,
            precipitation=precipitation,
            haze=haze,
            notes=notes,
            user_id=user_id
        )
        return jsonify({'message': 'Observation stored successfully', 'id': observation.id}), 201
    except Exception as e:
        # Catch any other unexpected errors
        print(f"Unexpected error during store observation: {e}")
        return jsonify({'message': 'Store observation failed due to an unexpected error'}), 500


@observation_blueprint.route('/<int:observation_id>', methods=['GET'])
def get_observation_by_id(observation_id):
    observation = ObservationService.get_observation(observation_id)
    if observation:
        result = ObservationSchema().dump(observation)
        return jsonify(result), 200
    else:
        return jsonify({"error": "Observation not found"}), 404

@observation_blueprint.route('/by_user_id/<int:user_id>', methods=['GET'])
def get_observations_by_user_id(user_id):
    list_of_observation = ObservationService.get_observations_by_user_id(user_id)
    if list_of_observation:
        result = ObservationSchema(many=True).dump(list_of_observation)
        return jsonify(result), 200
    else:
        return jsonify({"error": "Observation not found"}), 404


@observation_blueprint.route('/<int:observation_id>', methods=['PUT'])
def update_observation(observation_id):
    data = request.json
    observation = ObservationService.update_observation(observation_id, data['name'], data.get('description'))
    if observation:
        return jsonify(observation), 200
    return jsonify({"error": "Observation not found"}), 404


@observation_blueprint.route('/<int:observation_id>', methods=['DELETE'])
def delete_observation(observation_id):
    observation = ObservationService.delete_observation(observation_id)
    if observation:
        return jsonify({"success": "Observation deleted"}), 200
    return jsonify({"error": "Observation not found"}), 404
