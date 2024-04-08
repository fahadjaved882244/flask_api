"""
Name: Muhammad Fahad Javed
Date: 29/03/2024
Objective: Define the observation model
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Observation(Base):
  __tablename__ = 'observations'

  id = Column(Integer, primary_key=True)
  date_time = Column(DateTime, nullable=False)  # Stores date and time in ISO 8601 format
  time_zone_offset = Column(Integer, nullable=False)  # Stores offset in ISO 8601 format (e.g., UTC-10:00)
  latitude = Column(Float, nullable=False)
  longitude = Column(Float, nullable=False)
  land_surface_temperature = Column(Float)  # Temperature in degrees Celsius
  sea_surface_temperature = Column(Float)  # Temperature in degrees Celsius
  humidity = Column(Float)  # Humidity in g/kg
  wind_speed = Column(Float)  # Wind speed in km/h
  wind_direction = Column(Float)  # Wind direction in decimal degrees
  precipitation = Column(Float)  # Precipitation in mm
  haze = Column(Float)  # Haze percentage
  notes = Column(Text)
  
  user_id = Column(Integer, ForeignKey('users.user_id'))
  user = relationship("User")  # Relationship with User model

  def __repr__(self):
    return '<Observation %r>' % self.observation_id

