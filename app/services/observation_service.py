from app import db
from app.models.observation_model import Observation

class ObservationService:
  @staticmethod
  def create_observation(
    date_time,
    time_zone_offset,
    latitude,
    longitude,
    land_surface_temperature,
    sea_surface_temperature,
    humidity,
    wind_speed,
    wind_direction,
    precipitation,
    haze,
    notes,
    user_id,
    ):
    try:
      new_observation = Observation(
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
      db.session.add(new_observation)
      db.session.commit()
      return new_observation
    except Exception as e:
      db.session.rollback()
      # Log the error as appropriate
      print(f"Error creating Observation: {e}")
      return None

  @staticmethod
  def get_observation(observation_id):
    return Observation.query.filter_by(id=observation_id).first()
  
  @staticmethod
  def get_observations_by_user_id(user_id):
    return Observation.query.filter_by(user_id=user_id).all()

  @staticmethod
  def update_observation(observation_id, name, description):
    observation = Observation.query.filter_by(id=observation_id).first()
    if observation:
        observation.name = name
        observation.description = description
        db.session.commit()
    return observation

  @staticmethod
  def delete_observation(observation_id):
    observation = Observation.query.filter_by(id=observation_id).first()
    if observation:
        db.session.delete(observation)
        db.session.commit()
    return observation
