from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import InputRequired, Required
from jinja2 import Markup

class dlOptions(FlaskForm):
    """
    Define and prepare all
    download options
    """
    # url
    videoUrl = StringField('videoUrlBoid', validators=[InputRequired()])

    # video quality
    quality_dict = [('0', Markup('Select Quality')), \
                     ('Max', 'Maximum'), \
                     ('Min', 'Minimum')]
    quality_list = SelectField('Select Quality',
                               choices=quality_dict,
                               validators=[Required()])

    # file format
    format_dict = [('0', Markup('Select Format')),
                   ('mp3', 'Mp3'),
                   ('mp4', 'Mp4')]
    format_list = SelectField('Select Format',
                              choices=format_dict,
                              validators=[Required()])

    # Download playlist (boolean)
    dl_playlist_dict = [('0', Markup('Download PLaylist ?')),
                        ('yes', 'Yes'),
                        ('no', 'No')]
    dl_playlist = SelectField('Download PLaylist',
                              choices=dl_playlist_dict,
                              validators=[Required()])

    submit = SubmitField('Launch')

