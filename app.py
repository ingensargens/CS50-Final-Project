import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import subprocess
import os
from lyricsgenius import Genius
import helpers
from helpers import setup, draw_text_on_image
# to run you must pip install spotipy, flask, flask-session, subprocess, lyricsgenius, and pillow 
#run setup cmds
setup()

#genius
genius = Genius(f'{os.environ.get("GENIUS_TOKEN")}')
genius.verbose = True
#spotify auth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(redirect_uri='http://localhost:5000/', scope="user-top-read user-read-recently-played user-read-currently-playing user-library-read"))

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


@app.route('/selected_lyrics', methods=['POST', 'GET'])
def selected_lyrics():
    if request.method == "POST":
        selected_lyrics = request.form.getlist('selected_lyrics')
        color = request.form.get('colorPicker')
        fntSize = int(request.form.get('fontSize'))
        name = request.form.get('bg')
        font = request.form.get('font')
        print(name)
        draw_text_on_image(selected_lyrics, color=color, size=fntSize, img=name,font=font)
        if len(selected_lyrics) <= 6:
            return render_template('lyricsSelected.html', selected_lyrics=selected_lyrics)
        else:
            return "You can only select up to 6 lyrics. Please go back and select fewer lyrics."

@app.route('/recommend', methods=['GET'])#,'POST'])
def recommend():
    
    top_tracks = sp.current_user_top_tracks(time_range='long_term', limit=5)
    top_artists = sp.current_user_top_artists(time_range='long_term', limit=5)

    seed_tracks = [track['uri'] for track in top_tracks['items']]
    seed_artists = [artist['uri'] for artist in top_artists['items']]

    recommended_tracks = sp.recommendations(seed_tracks=seed_tracks)
    recommended_by_artists = sp.recommendations(seed_artists=seed_artists)
    
    # recommended_tracks = [track['name'] for track in recommended_tracks['tracks']]
    # recommended_by_artists = [track['name'] for track in recommended_by_artists['tracks']]
    print(recommended_tracks['tracks'][0]['external_urls']['spotify'])
    return render_template('recommender.html', recommended_tracks=recommended_tracks, recommended_by_artists=recommended_by_artists)
    # sp.recommendations()
    # else: #POST


if __name__ == '__main__':
    app.run(debug=True, port=5010)
