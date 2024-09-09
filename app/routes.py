from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """
    @brief Handles the home page route.

    @return Renders the index template for the home page.
    """
    return render_template('index.html')
