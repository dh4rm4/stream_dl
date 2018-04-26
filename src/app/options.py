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
                     ('1', 'Maximum'), \
                     ('2', 'Minimum')]
    quality_list = SelectField('Select Quality',
                               choices=quality_dict,
                               validators=[Required()])

    # file format
    format_dict = [('0', Markup('Select Format')),
                   ('1', 'Mp3'),
                   ('2', 'Mp4')]
    format_list = SelectField('Select Format',
                              choices=format_dict,
                              validators=[Required()])

    # Download playlist (boolean)
    dl_playlist_dict = [('0', Markup('Download PLaylist ?')),
                        ('1', 'Yes'),
                        ('2', 'No')]
    dl_playlist = SelectField('Download PLaylist',
                              choices=dl_playlist_dict,
                              validators=[Required()])

    submit = SubmitField('Launch')
    
