from flask_bcrypt import Bcrypt 


bcrypt = Bcrypt()
blacklist = set()



def generate_password_hash(password):
    my_hash = bcrypt.generate_password_hash(password)
    return my_hash

def check_password_hash(password):
    pass



