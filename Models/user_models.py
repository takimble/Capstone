

import datetime
from . import db

from marshmallow import Schema, fields

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(300), unique = True)
    password = db.Column(db.String(100))
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(30))


    def __init__(self,email,password,fname,lname ):
        self.email = email
        self.password = password
        self.fname = fname
        self.lname = lname
     
    def save(self):
        db.session.add(self)
        db.session.commit()
        return 'User sucecesfully created'
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return 'Bill has been deleted'
    
    def update(self, old, data):
        for key, item in data.items():
            setattr(old, key, item)
        db.session.commit()
        return old
    
    @staticmethod
    def find_all_users():
        return User.query.all()

    @staticmethod
    def find_one_user(post_id):
        return User.query.filter_by(id=post_id).first()


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    fname = fields.Str(required=True)



