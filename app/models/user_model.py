"""
Name: Muhammad Fahad Javed
Date: 29/03/2024
Objective: Define the observer model
"""

from app import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  email = db.Column(db.String(64), nullable=False, unique=True)
  hash_password = db.Column(db.String(255), nullable=False)
  name = db.Column(db.String(64), nullable=True)
  is_email_verified = db.Column(db.Boolean, default=False)
  is_qualified = db.Column(db.Boolean, default=False)

  # Establish a relationship to the Observation model
  observations = db.relationship('Observation', back_populates='user', lazy='dynamic')

  def __repr__(self):
    return '<User %r>' % self.user_id

