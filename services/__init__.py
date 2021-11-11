"""
Test Eiya
"""
import os

from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from .models import db
from .models.vehiculo import Vehiculo

from services.api.vehiculos import vehiculo

def create_app(config) -> Flask:
    app = Flask(__name__, template_folder="../templates")

    app.config.from_object(config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@127.0.0.1:5432/eiya'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

    CORS(app)

    with app.app_context():
        db.init_app(app)
        db.create_all()
        Migrate(app, db, directory="services/migrations")

    app.register_blueprint(vehiculo, url_prefix='/api')

    return app
