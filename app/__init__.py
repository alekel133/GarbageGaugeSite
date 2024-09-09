from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .routes import main_bp
from config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)
migrate.init_app(app, db)

# Register blueprints
app.register_blueprint(main_bp)
