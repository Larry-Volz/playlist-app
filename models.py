"""Models for Playlist app.""" 

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app 
    db.init_app(app)


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlists'
    def __repr__(self):
           return f"id={self.id} name={self.name} description={self.description}" 

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.Text, nullable=True)

    songs = db.relationship('Song', secondary='playlistsongs', backref='playlists')

    # in case info on mapping table is ever desired
    # assignments = db.relationship('PlaylistSong',
    #                               backref='playlist')


class Song(db.Model):
    """Song."""
    __tablename__ = 'songs'
    def __repr__(self):
           return f"id={self.id} title={self.title} artist={self.artist}" 

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(60), nullable=False)
    artist = db.Column(db.String(60), nullable=True)

    # assignments = db.relationship('PlaylistSong',
    #                               backref='song')

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlistsongs'
    def __repr__(self):
           return f"id={self.id} playlist_id={self.playlist_id} song_id={self.song_id}" 

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)



    


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
