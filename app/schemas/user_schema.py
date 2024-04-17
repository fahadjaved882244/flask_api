from app import ma
from marshmallow import fields, validate, validates, ValidationError

class RegisterUserSchema(ma.Schema):
  email = fields.Email(required=True)
  password = fields.Str(required=True, validate=validate.Length(min=8, max=24))
  name = fields.Str(required=True, validate=validate.Length(min=3, max=64))

class LoginUserSchema(ma.Schema):
  email = fields.Email(required=True)
  password = fields.Str(required=True)