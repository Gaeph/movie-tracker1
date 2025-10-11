import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from sqlalchemy import MetaData

# Définir chemin absolu
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Création de l'application Flask
app = Flask(__name__)

# Configuration base de données
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

# Convention de nommage pour SQLAlchemy
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Initialisation de la base de données
db = SQLAlchemy(metadata=metadata)
db.init_app(app)

# Migration
migrate = Migrate(app, db)

# API RESTful et CORS
api = Api(app)
CORS(app)
