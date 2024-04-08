from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import SQLAlchemyError
from app.models.user_model import User
from app import db

class UserService:
    @staticmethod
    def create_user(email: str, password: str, name: str) -> User:
        """
        Create a new user with the given email, password, and name.
        Handles exceptions to prevent application crash on database errors.
        """
        try:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(email=email, hash_password=hashed_password, name=name)
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as e:
            db.session.rollback()
            # Log the error as appropriate
            print(f"Error creating user: {e}")
            return None

    @staticmethod
    def authenticate_user(email: str, password: str) -> bool:
        """
        Check if the given email and password correspond to a valid user.
        Handles exceptions to ensure application stability.
        """
        try:
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.hash_password, password):
                return True
            return False
        except Exception as e:
            # Log the error as appropriate
            print(f"Error authenticating user: {e}")
            return False

    @staticmethod
    def get_user_by_email(email: str) -> User:
        """
        Retrieve a user by their email address.
        Handles exceptions to ensure application stability.
        """
        try:
            return User.query.filter_by(email=email).first()
        except Exception as e:
            # Log the error as appropriate
            print(f"Error fetching user by email: {e}")
            return None
