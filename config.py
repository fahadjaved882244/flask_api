import os
from datetime import timedelta

class Config:
    # Base directory where the script runs
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # Secret key for signing session cookies
    SECRET_KEY = os.urandom(32)
    
    # ORM Configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    
    # Secret key for JWT encoding and decoding
    JWT_SECRET_KEY = '234JSNNI&23etsdvsc_k?$#^&@(@)ey_h@!#(*@!#(*@!#*!ere'  # Ideally fetched from environment variable
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    
    RUN_TESTS_BEFORE_SERVER = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.BASE_DIR, 'dev.db')
    RUN_TESTS_BEFORE_SERVER = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.BASE_DIR, 'test.db')
   
    # Use a separate secret key for testing
    SECRET_KEY = 'test_secret_key_234JSNNI&23etsdvsc_k?$#^&@(@)'
   
    # Use a simple and fast hashing algorithm
    BCRYPT_LOG_ROUNDS = 4
    
    # Disable JWT expiration during tests to simplify requests
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.BASE_DIR, 'prod.db')
    
    # Log rounds and JWT expiration are typically longer in production
    BCRYPT_LOG_ROUNDS = 12
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
