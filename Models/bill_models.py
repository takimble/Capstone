
from . import db
import datetime

from marshmallow import Schema, fields

class Bills(db.Model):
    __tablename__ = 'bills'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String())
    due = db.Column(db.DateTime)
    amount = db.Column(db.Integer)
    paid = db.Column(db.String())
    date_created = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__ (self, title, due,amount, paid, date_created,user_id):
        self.title = title
        self.due = due
        self.amount = amount
        self.paid = paid
        self.date_created = date_created
        self.user_id = user_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return ' Bill has been saved'

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
    def all_bills():
        return Bills.query.all()

    @staticmethod
    def single_bill(post_id):
        return Bills.query.filter_by(id=post_id).first()

class BillSchema(Schema):
    id = fields.Int(dump_only = True)
    title = fields.Str(required=True)
    amount= fields.Int(required=True)
    due = fields.DateTime(dump_only=True)
    paid = fields.Boolean(required=True)
    date_created = fields.DateTime(dump_only=True)
    user_id = fields.Str(required=True)








    