import os

class Config:
    """
    Base configuration class. This class contains configuration settings that are common to all environments.
    """

    # Secret key for session management and CSRF protection
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Other configurations
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads/')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class DevelopmentConfig(Config):
    """
    Configuration settings for development.
    """
    DEBUG = True
    ENV = 'development'

class TestingConfig(Config):
    """
    Configuration settings for testing.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    DEBUG = False
    ENV = 'testing'

class ProductionConfig(Config):
    """
    Configuration settings for production.
    """
    DEBUG = False
    ENV = 'production'
    # You might want to add additional settings for production here
