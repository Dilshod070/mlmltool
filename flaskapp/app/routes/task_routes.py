from flask import render_template, redirect, url_for
from flask_login import current_user, login_required

from app import app, db
from app.core import count_priority
from app.forms import NewTaskForm
from app.models import User, Task


@app.route("/my-tasks/list")
@login_required
def task_list():
    my_id = int(current_user.get_id())
    my_tasks = list(User.query.get(my_id).tasks.all())
    for task in my_tasks:
        setattr(task, 'priority', count_priority(task))
    my_tasks = sorted(my_tasks, key=lambda x: x.priority, reverse=True)
    return render_template('task_list.html', title='List of Tasks', tasks=my_tasks)


@app.route("/my-tasks/create", methods=['GET', 'POST'])
@login_required
def task_create():
    form = NewTaskForm()
    if form.validate_on_submit():
        task = Task(
            name=form.name.data, user_id=int(current_user.get_id()),
            complexity=form.complexity.data, importance=form.importance.data, urgency=form.urgency.data,
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('task_list'))
    return render_template('task_create.html', title='New Task', form=form)
