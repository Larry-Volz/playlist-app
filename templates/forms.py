from flask_wtf import FlaskForm
from wtforms import StringField, validators, HiddenField
from wtforms.validators import InputRequired, Optional

class PlaylistForm(FlaskForm):
    """For making a playlist"""

    name = StringField("Create a playlist", validators = [InputRequired(message = "cannot be blank")])

    description = StringField("Tell us about it")

 

