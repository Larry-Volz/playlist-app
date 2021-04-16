"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms import StringField, validators, HiddenField
from wtforms.validators import InputRequired, Optional


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Create a playlist", validators = [InputRequired(message = "cannot be blank")])

    description = StringField("Tell us about it")


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song title", validators = [InputRequired(message = "cannot be blank")])

    artist = StringField("Artist", validators = [InputRequired(message = "cannot be blank")])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
