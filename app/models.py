from . import db

class User(db.Model):
    """
    @brief Defines a User Model for the application

    @details The User model stores user information in the database

    @param id The user's unique identifier
    @param username The username of the user
    """

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
