from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
from wtforms.fields.html5 import DecimalRangeField
from wtforms.validators import DataRequired, Optional, NumberRange


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class NewTaskForm(FlaskForm):
    name = StringField('Task Goal', validators=[DataRequired()])
    complexity = DecimalRangeField('Task Complexity (0-10)', validators=[NumberRange(min=0, max=100)])
    importance = DecimalRangeField('Task Importance (0-10)', validators=[NumberRange(min=0, max=100)])
    urgency = DecimalRangeField('Task Urgency (0-10)', validators=[NumberRange(min=0, max=100)])
    submit = SubmitField('Create')
