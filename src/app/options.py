from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import StringField
from wtforms.validators import InputRequired

class dlOptions(FlaskForm):
    videoUrl = StringField('videoUrlBoid', validators=[InputRequired()])
    submit = SubmitField('Launch')
