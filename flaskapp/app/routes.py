from flask import render_template

from main import app, db


@app.route("/")
@app.route("/index")
def hello():
    text = f"Hello World from Updated Flask.</br>"
    text += "<a href='/users'>link to users</a></br>"
    return text


@app.route("/users")
def users():
    user = {'username': 'dilshod'}
    tasks = [
        {'title': 'makeup'},
        {'title': 'homework'},
        {'title': 'wash dishes'},
    ]
    return render_template('users.html', user=user, tasks=tasks)
