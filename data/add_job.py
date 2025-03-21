from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    job = StringField('Job Title', validators=[DataRequired()])
    team_leader = StringField('Team Leader id', validators=[DataRequired()])
    work_size = StringField('Work Size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    remember_me = BooleanField('Is job finished?')
    submit = SubmitField('Submit')