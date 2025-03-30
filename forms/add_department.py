from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import EmailField
from wtforms.validators import DataRequired


class AddDepartmentForm(FlaskForm):
    title = StringField('Department Title', validators=[DataRequired()])
    members = StringField('Members', validators=[DataRequired()])
    department_email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')
