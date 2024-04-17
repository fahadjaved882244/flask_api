"""
Name: Muhammad Fahad Javed
Date: 29/03/2024
Objective: Define the observation model
"""

from app import db

class Observation(db.Model):
  __tablename__ = 'observations'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  date_time = db.Column(db.DateTime, nullable=False)  # Stores date and time in ISO 8601 format
  time_zone_offset = db.Column(db.Integer, nullable=False)  # Stores offset in ISO 8601 format (e.g., UTC-10:00)
  latitude = db.Column(db.Float, nullable=False)
  longitude = db.Column(db.Float, nullable=False)
  land_surface_temperature = db.Column(db.Float, nullable=False)  # Temperature in degrees Celsius
  sea_surface_temperature = db.Column(db.Float, nullable=False)  # Temperature in degrees Celsius
  humidity = db.Column(db.Float, nullable=False)  # Humidity in g/kg
  wind_speed = db.Column(db.Float, nullable=False)  # Wind speed in km/h
  wind_direction = db.Column(db.Float, nullable=False)  # Wind direction in decimal degrees
  precipitation = db.Column(db.Float, nullable=False)  # Precipitation in mm
  haze = db.Column(db.Float, nullable=False)  # Haze percentage
  notes = db.Column(db.Text, nullable=True)
  
  # Foreign key to link to the User model
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  user = db.relationship('User', back_populates='observations')
    
  def __repr__(self):
    return '<Observation %r>' % self.observation_id

