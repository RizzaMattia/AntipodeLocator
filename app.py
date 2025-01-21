import os
from flask import Flask
from blueprints.api import app as api_app 
from blueprints.routes import app as routes_app

from flask_migrate import Migrate
from models.conn import db
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Registrazione del blueprint
app.register_blueprint(api_app, url_prefix='/api')
app.register_blueprint(routes_app, url_prefix='/')


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY',"TERCES")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
migrate = Migrate(app, db)
db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
