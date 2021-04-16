from models import db, Song, Playlist, PlaylistSong
from app import app



# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Playlist.query.delete()
Song.query.delete()
PlaylistSong.query.delete()

#Add songs
bohemian_rhapsody = Song(title='Bohemian Rhapsody', artist='Queen')
red_barchetta = Song(title='Red Barchetta', artist='Rush')

feel_good_inc = Song(title='Feel Good Inc.', artist='Gorillaz')
uptown_funk = Song(title='Uptown Funk', artist='Mark Ronson')

#Add playlists
classic_rock = Playlist(name='Classic Rock',description='music from the 60''s-80''s')
modern_rock = Playlist(name='Modern Rock', description='music from the last ten years')

#Add playlist-songs
BR_CR = PlaylistSong(playlist_id=1, song_id=1)
RB_CR = PlaylistSong(playlist_id=1, song_id=2)
FGI_MR = PlaylistSong(playlist_id=2, song_id=3)
UF_MR = PlaylistSong(playlist_id=2, song_id=4)

db.session.add(bohemian_rhapsody)
db.session.add(red_barchetta)
db.session.add(feel_good_inc)
db.session.add(uptown_funk)

db.session.add(classic_rock)
db.session.add(modern_rock)

db.session.commit()

db.session.add(BR_CR)
db.session.add(RB_CR)
db.session.add(FGI_MR)
db.session.add(UF_MR)

db.session.commit()