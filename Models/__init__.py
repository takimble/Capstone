from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BlackListToken(db.Model):
    __tablename__= 'blacklist_token'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self,token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return '<id:token:{}'.format(self.token)

    def add(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def is_blacklisted(cls,jti):
        query = cls.query.filter_by(jti=token).first()
        return bool(query)

