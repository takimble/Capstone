from Models.bill_models import BillSchema , Bills
import datetime

bill_schema = BillSchema()

def new_bill(data,user):
    post_bill = Bills(
        title=data['title'],
        due=data['due'],
        paid=data['paid'],
        amount=data['amount'],
        date_created=datetime.datetime.utcnow(),
        user_id=user)
    
    try:
        post_bill.save()
        message = {
            'Message': f'Bill was successfully posted'
        }
        return message, 200
    
    except Exception as e:
        return str(e), 400


def edit_bill(post_id, data):
    x = Bills.single_bill(post_id)
    updated = x.update(x,data)
    new_bill = bill_schema.dump(updated)
    return new_bill


def delete_bill(bill):
    x = Bills.single_bill(bill['id'])
    x.delete()
    return 'Deleted'


def get_bills():
    x = Bills.all_bills()
    bill_post = bill_schema.dump(x, many=True)
    return bill_post

def get_single_bill(post_id):
    x = Bills.single_bill(post_id)
    bill_post = bill_schema.dump(x)
    return bill_post

