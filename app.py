from flask import Flask


from Models import db 
from Services import bcrypt

from Controllers import jwt
from Controllers.user_controller import user_blueprint
from Controllers.bill_controller import bills_blueprint
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand





app = Flask(__name__)

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)


app.config.from_object('config.Development')
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']





migrate = Migrate(app, db)


manager = Manager(app)

manager.add_command('db', MigrateCommand)


#Blueprints
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(bills_blueprint, url_prefix='/bills')



if __name__ == "__main__":
    app.run()