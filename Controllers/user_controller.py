from flask import Blueprint, request
from flask_jwt_extended import create_refresh_token, get_raw_jwt, create_access_token, get_jwt_identity, jwt_required, jwt_refresh_token_required

from Services.user_service import create_user, delete, get_users, get_one_user, edit_user
from Services import bcrypt
from Models.user_models import User

from Services import blacklist


user_blueprint = Blueprint('user_api', __name__)

@user_blueprint.route('/login', methods=['POST'])
def login():
    body = request.json
    email = body['email']

    check = User.query.filter_by(email=email).first()

    if bcrypt.check_password_hash(check.password, password=body['password']):
        access_token = create_access_token(check.id)
        refresh_token = create_refresh_token(check.id)
        return {
            'message': 'Log in successful!',
            'token': access_token,
            'refresh': refresh_token
        }
    else:
        return {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }



@user_blueprint.route('/register', methods=['POST'])
def register():
    body = request.json
    message = create_user(
        body['email'],
        bcrypt.generate_password_hash(body['password']).decode('utf-8'),
        body['fname'],
        body['lname'])

    return {
        'message': message
    }



@user_blueprint.route('/modify:<int:post_id>', methods=['GET','PUT','DELETE'])
@jwt_required
def user_view(post_id):
# VIEW 
    if request.method == 'GET':
        findd = get_one_user(post_id)
        if findd:
            return findd
        else:
            return 'User not found'
# EDIT
    elif request.method == 'PUT':
        data = request.json
        user = get_jwt_identity()
        user_info = get_one_user(post_id)
        if str(user) == user_info['id']:
            return edit_user(post_id, data), 'User is up to date'
# DELETE
    elif request.method == 'DELETE':
        user = get_jwt_identity()
        user_info = get_one_user(post_id)
        if str(user) == user_info['id']:
            return delete(user_info)
        else:
            return 'Method not authorized'
    
    else:
        return 'METHOD NOT ALLOWED'

@user_blueprint.route('/all', methods=['GET'])
@jwt_required
def view_all_users():
    x = get_users()
    return str(x)



@user_blueprint.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user= get_jwt_identity()
    access_token = create_access_token(current_user)
    return 'Refresh', access_token

@user_blueprint.route('/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return 'log out succesfull'

@user_blueprint.route('/logout2', methods=['DELETE'])
@jwt_refresh_token_required
def logout2():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return 'log out succesfull'

@user_blueprint.route('/protected', methods=['GET'])
@jwt_required
def protected():
    return 'test works'