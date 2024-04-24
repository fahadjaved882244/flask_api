import pytest
from app import create_app
from config import TestingConfig

@pytest.fixture(scope='module')
def test_client():
  # Ensure you have a configuration for testing that can use an in-memory database
  flask_app = create_app(config_class=TestingConfig)

  # Flask provides a way to test your application by exposing the Werkzeug test Client
  testing_client = flask_app.test_client()

  # Establish an application context before running the tests.
  ctx = flask_app.app_context()
  ctx.push()

  # this is where the testing happens!
  yield testing_client

  ctx.pop()