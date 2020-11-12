from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app, db
from app.forms import LoginForm
from app.models import User


@app.route("/")
@app.route("/index")
def hello():
    return render_template('index.html')


@app.route("/users")
@login_required
def users():
    app_users = list(User.query.all())
    return render_template('users.html', users=app_users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('hello'))

    form = LoginForm()
    if form.validate_on_submit():
        is_newly_registered = True
        correct_data = True

        # Search for user in database
        password_hash = User.get_password_hash(form.password.data)
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('hello'))
        elif user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('hello'))

    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('hello'))