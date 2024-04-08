import os
from datetime import timedelta

# Secret key for signing session cookies
SECRET_KEY = os.urandom(32)

# Base directory where the script runs
base_dir = os.path.abspath(os.path.dirname(__file__))

# On changes it will refresh
DEBUG = True

# ORM Configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'db.sqlite')
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret key for JWT encoding and decoding
JWT_SECRET_KEY = '234JSNNI&23etsdvsc_k?$#^&@(@)ey_h@!#(*@!#(*@!#*!ere'  # Change this to a random secret key
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)  # Set the expiration time for access tokens
