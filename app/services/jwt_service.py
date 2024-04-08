from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

class JWTService:
    @staticmethod
    def generate_tokens(user_email: str):
        """
        Generate access and refresh tokens for the given user identifier.
        """
        access_token = create_access_token(identity=user_email)
        refresh_token = create_refresh_token(identity=user_email)
        return access_token, refresh_token

    @staticmethod
    @jwt_required()
    def get_current_user():
        """
        Retrieve the current user's identity from the access token.
        """
        current_user_email = get_jwt_identity()
        return current_user_email
