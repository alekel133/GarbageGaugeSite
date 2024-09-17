from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from app.models import get_user_by_username, db, User

auth_bp = Blueprint('auth', __name__, template_folder="../templates/auth")

@auth_bp.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Get the user by username
        user = get_user_by_username(username)

        if user and user.check_password(password):
            login_user(user)
            redirect(url_for('main.home'))
        else:
            flash('Invalid username or password')

    return render_template(url_for('main.home'))

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@auth_bp.route('/register', methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if get_user_by_username(username):
            flash("Username already exists.")
            return(redirect(url_for("auth.register")))

        new_user = User(username=username)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template(url_for("auth.login"))
