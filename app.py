import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import subprocess
import os
from lyricsgenius import Genius
import helpers
from helpers import setup

#run setup cmds
setup()

#genius
genius = Genius(f'{os.environ.get("GENIUS_TOKEN")}')
genius.verbose = True
#spotify auth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(redirect_uri='http://localhost:5010/', scope="user-top-read user-read-recently-played user-read-currently-playing user-library-read"))

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


#routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lyrics', methods=["GET", "POST"])
def lyrics():
    if request.method == "GET":
        return render_template('lyricsSearch.html')
    else: #method = post
        song = request.form.get("song_query")
        song = genius.search_song(title=song)
        songArtist = song.artist
        songLyrics = song.lyrics
        songLyrics = songLyrics[songLyrics.find('['):].split('\n')

        filter_text = f'See {songArtist} Live'

        for k in songLyrics:
            if (filter_text in k) or (k == ''):
                songLyrics.remove(k)

        return render_template('lyrics.html', lyrics=songLyrics)


@app.route('/selected_lyrics', methods=['POST'])
def selected_lyrics():
    selected_lyrics = request.form.getlist('selected_lyrics')
    if len(selected_lyrics) <= 6:
        return render_template('lyricsSelected.html', selected_lyrics=selected_lyrics)
    else:
        return "You can only select up to 6 lyrics. Please go back and select fewer lyrics."



if __name__ == '__main__':
    app.run(debug=True, port=5010)



# 4 weeks
# results1 = sp.current_user_top_tracks(time_range='short_term', limit=5)
# for item in results1['items']:
#     print(item['name'])
# 6 months
# results2 = sp.current_user_top_tracks(time_range='medium_term', limit=5)
# for item in results2['items']:
#     print(item['name'])
# all time
# results3 = sp.current_user_top_tracks(time_range='long_term', limit=5)
# for item in results3['items']:
#     print(item['name'])
# print('\n')