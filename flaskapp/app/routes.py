from flask import render_template, flash, redirect, url_for

from main import app, db
from forms import LoginForm
from models import User


@app.route("/")
@app.route("/index")
def hello():
    return render_template('index.html')


@app.route("/users")
def users():
    users = list(User.query.all())
    return render_template('users.html', users=users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        is_newly_registered = True
        correct_data = True

        # Search for user in database
        password_hash = User.get_password_hash(form.password.data)
        user = User(username=form.username.data, password_hash=password_hash)
        for u in User.query.all():
            if u.username == user.username:
                is_newly_registered = False
                if u.password_hash != user.password_hash:
                    correct_data = False

        # If User is new, save him in database
        if is_newly_registered:
            db.session.add(user)
            db.session.commit()

        # Show message
        flash('Login requested for user {}, remember_me={} newly_registered={} correct_password={}'.format(
            form.username.data, form.remember_me.data, is_newly_registered, correct_data
        ))

        return redirect(url_for('hello'))
    return render_template('login.html', title='Sign In', form=form)
