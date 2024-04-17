from app import ma
from marshmallow import fields, validate, validates, ValidationError
from marshmallow.validate import Range, Length

class ObservationSchema(ma.Schema):
  date_time = fields.DateTime(required=True)
  time_zone_offset = fields.Integer(required=True)
  latitude = fields.Float(required=True, validate=Range(min=-90.0, max=90.0))
  longitude = fields.Float(required=True, validate=Range(min=-180.0, max=180.0))
  land_surface_temperature = fields.Float(required=True)
  sea_surface_temperature = fields.Float(required=True)
  humidity = fields.Float(required=True)
  wind_speed = fields.Float(required=True)
  wind_direction = fields.Float(required=True)
  precipitation = fields.Float(required=True)
  haze = fields.Float(required=True)
  notes = fields.String(validate=Length(max=511))
  
  
class GetObservationSchema(ma.Schema):
  id = fields.Integer(required=True)
  date_time = fields.DateTime(required=True)
  time_zone_offset = fields.Integer(required=True)
  latitude = fields.Float(required=True, validate=Range(min=-90.0, max=90.0))
  longitude = fields.Float(required=True, validate=Range(min=-180.0, max=180.0))
  land_surface_temperature = fields.Float(required=True)
  sea_surface_temperature = fields.Float(required=True)
  humidity = fields.Float(required=True)
  wind_speed = fields.Float(required=True)
  wind_direction = fields.Float(required=True)
  precipitation = fields.Float(required=True)
  haze = fields.Float(required=True)
  notes = fields.String(validate=Length(max=511))