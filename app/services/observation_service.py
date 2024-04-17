from app import db
from app.models.observation_model import Observation
from app.models.user_model import User


class ObservationService:
  @staticmethod
  def create_observation(
    user_id,
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
    ):
    try:
      new_observation = Observation(
        user_id=user_id,
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
        notes=notes
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
  def get_observations_by_user_email(user_email: str):
    user = User.query.filter_by(email=user_email).first()
    if not user:
        return None
    return user.observations
  
  @staticmethod
  def get_observations_by_user_id_and_observation_id(user_id: int, observation_id: int):
    observation = Observation.query.filter_by(user_id=user_id, id=observation_id).first()
    if not observation:
        return None
    return observation

  @staticmethod
  def update_observation(
    observation_id,
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
    ):
    observation = Observation.query.filter_by(id=observation_id).first()
    if observation:
      # Update observation details
      observation.date_time = date_time
      observation.time_zone_offset = time_zone_offset
      observation.latitude = latitude
      observation.longitude = longitude
      observation.land_surface_temperature = land_surface_temperature
      observation.sea_surface_temperature = sea_surface_temperature
      observation.humidity = humidity
      observation.wind_speed = wind_speed
      observation.wind_direction = wind_direction
      observation.precipitation = precipitation
      observation.haze = haze
      observation.notes = notes

      # Try committing changes to the database
      try:
        db.session.commit()
        return observation
      except Exception as e:
        # Rollback in case of error
        db.session.rollback()
        print(f"Failed to update observation: {e}")
        return None


  @staticmethod
  def delete_observation(observation_id):
    observation = Observation.query.filter_by(id=observation_id).first()
    if observation:
        db.session.delete(observation)
        db.session.commit()
    return observation
