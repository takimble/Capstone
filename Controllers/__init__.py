from flask_jwt_extended import JWTManager
from Services import blacklist

jwt= JWTManager()

from .user_controller import user_blueprint
from .bill_controller import bills_blueprint


@jwt.token_in_blacklist_loader
def check_token_to_blacklist(decrypted_token):
    jti= decrypted_token['jti']
    return jti in blacklist