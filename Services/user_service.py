

from Models.user_models import User, UserSchema
 
user_schema = UserSchema()

def create_user(email,password, fname,lname):
    new_user = User(email,password,fname,lname)
    return new_user.save() 


def edit_user(post_id,data):
    x = User.find_one_user(post_id)
    edit = x.update(x,data)
    updated= user_schema.dump(edit)
    return updated


def delete(user):
    x = User.find_one_user(user['id'])
    x.delete()
    return 'User successfully deleted'

def get_users():
    x = User.find_all_users()
    user_list = user_schema.dump(x, many=True)
    return user_list

def get_one_user(post_id):
    x = User.find_one_user(post_id)
    find = user_schema.dump(x)
    return find

