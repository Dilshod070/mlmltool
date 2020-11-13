from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
from wtforms.validators import DataRequired, Optional


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class NewTaskForm(FlaskForm):
    name = StringField('Task Goal', validators=[DataRequired()])
    complexity = FloatField('Task Complexity (0-10', validators=[Optional()])
    importance = FloatField('Task Importance (0-10', validators=[Optional()])
    urgency = FloatField('Task Urgency (0-10', validators=[Optional()])
    submit = SubmitField('Create')
