import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import subprocess
import os
from lyricsgenius import Genius


#run setup cmds
def setup():

    # Specify the path to your commands.txt file
    commands_file_path = "commands.txt"

    # Read and process the commands from the file
    with open(commands_file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("export "):
                key, value = line[len("export "):].split("=", 1)
                os.environ[key] = value
setup()

#genius
genius = Genius(f'{os.environ.get("GENIUS_TOKEN")}')

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

@app.route('/lyrics')
def lyrics():
    return render_template('lyrics.html')

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