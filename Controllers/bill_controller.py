from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from Services.bill_service import new_bill, get_bills,get_single_bill,edit_bill,delete_bill



bills_blueprint = Blueprint('bills_api', __name__)

@bills_blueprint.route('/new', methods=['POST'])
@jwt_required
def create_bill():
    user = get_jwt_identity()
    data = request.json

    return new_bill(data,user)


@bills_blueprint.route('/all', methods=['GET'])
@jwt_required
def view_all():
    x=get_bills()
    return str(x)


@bills_blueprint.route('/modify:<int:post_id>', methods=['GET','PUT', 'DELETE'])
@jwt_required
# VIEW
def bill_view(post_id):
    if request.method == 'GET':
        bill = get_single_bill(post_id)
        if bill:
            return bill
# EDIT
    elif request.method == 'PUT':
        data = request.json
        user = get_jwt_identity()
        bill = get_single_bill(post_id)
        if str(user) == bill['user_id']:
            return edit_bill(post_id, data)
# DELETE
    elif request.method == 'DELETE':
        user = get_jwt_identity()
        bill = get_single_bill(post_id)
        if str(user) == bill['user_id']:
            return delete_bill(bill),'Bill has been deleted'
        else:
            return 'Method not authorized'

    else:
        return 'METHOD NOT ALLOWED'
  








