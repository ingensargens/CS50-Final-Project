# Final Project - Rankings and Recommendations
## Overview
My final project is a flask **Spotify-data inspired** [final project](https://cs50.harvard.edu/x/2023/project/#getting-started) project for [CS50 - Harvard's Introduction to Computer Science Course](https://cs50.harvard.edu/x/2023/). My flask webpage incorporates 3 main features: a homepage which displays a user's top songs and top artists, song recommendations based on a user's top songs and top artists, and a lyrics search engine which can display lyrics on an image (mostly for aesthetic purposes).

An explanation and demonstration video can be found [here](https://youtu.be/Q-Gbthrm2bg).

## Spotify Authentication

When you first run the application, you'll be greeted by a green Spotify logo. Click this Spotify logo to allow (grant permission for) my application to access your Spotify data. Not authenticating or clicking any of the navbar buttons will not allow my program to access any of your data and will cause an error.

### NOTE: Running this without a spotify client id or client secret will not work.

## Top songs and artists 

The first feature of my application is rankings of your top songs and top artists. This feature is under the `home` tab of the app. Select a type of ranking (either song or artist) and a time period (4 weeks, 6 months, or all time) and then click generate. A ranking will be displayed based on your selections. This can be refreshed or gone back to by clicking home in the navbar.

## Lyrics

The main feature of this project is the Lyrics feature. Upon clicking on `lyrics` in the navbar, you are directed to a page where you can input a song. Entering a song in this format: `Song Name - Artist` provides more accurate results. 

After clicking `Search for Lyrics`, a list of the songs lyrics is loaded on the left side, along with a selection menu on the right side. Select up to 6 lyrics using the checkboxes. Then select a font color, font size, a background for your image, and a font to use. Upon clicking generate, an image is generated with the selected lyrics on the background you select. Clicking download will put it into your downloads folder. If the entire text does not fit, try changing the font size (default is 18).

## Recommendations

The last feature of my project is the recommendations tab. This provides song recommendations based on your top songs and top artists. It will only show 20 songs per column each time, but refreshing or clicking `recommendation` again provides new results.

## Credits

- The images for the backgrounds were all found publicly on Pinterest.
- The Spotify logo is from Spotify's website.
- The 3 different fonts were all found on fontspace.com. License: Freeware, Non-Commercial
	- link: https://www.fontspace.com/halimun-font-f30001
	- link: https://www.fontspace.com/tomatoes-font-f29709
	- link: https://www.fontspace.com/hello-ketta-font-f41129
- Code help from flask docs, stack overflow, Python Docs, Spotify Docs, Lyric Genius Docs, w3Schools, and CS50's duck debugger and ChatGPT (mostly CSS help)
- A lot of credit to [CS50 Lecture 9](https://www.youtube.com/watch?v=oVA0fD13NGI); I referred to this almost every time I worked with the routes in flask.

## How to use
#### Run each of the following in your command line.

```bash 
git clone https://github.com/ingensargens/finalProject.git
cd finalProject
pip install -r requirements.txt
```

#### Next, you will need to get Spotify API Client ID and Secret

Instructions on how to obtain these can be found [here](https://developer.spotify.com/documentation/web-api/concepts/apps)

Also make sure to add a redirect uri on the Spotify dashboard and set it as:
`http://127.0.0.1:5000/callback`

Replace CLIENT_ID_HERE and CLIENT_SECRET_HERE with the Spotify Generated Client ID and Client Secret (without quotation marks) into commands_template.txt as seen here: 
```
export SPOTIPY_CLIENT_ID=CLIENT_ID_HERE
export SPOTIPY_CLIENT_SECRET=CLIENT_SECRET_HERE
export SPOTIPY_REDIRECT_URI=http://127.0.0.1:5000/callback
```

#### Next, you will need to get a lyrics Genius API token:

Instructions on how to obtain a genius token can be found [here](https://lyricsgenius.readthedocs.io/en/master/setup.html#installation)

Replace GENIUS_TOKEN_HERE with the API generated Genius Token in commands_template.txt (including the quotations):
```
export GENIUS_TOKEN='GENIUS_TOKEN_HERE'
```

#### VERY IMPORTANT - IF YOU DO NOT DO THIS THE APP WILL NOT WORK
#### Now rename commands_template.txt to commands.txt
#### Now you can run the program using:
`python app.py` or `flask run` if in a venv.

## Improvements
I have been working on this project for around 6 months. As fun as its been, it is in a spot where I am happy to submit it with ease of mind. Here are a few improvements I could/plan to make:
- Adding the artist and song name under the image generated.
- Disabling the navbar before authentication.
- Understand/set up a virtual environment more accurately
- A lot of CSS improvements in terms of visual appeal.
- Making the loading time faster / making the page flow less complicated.
- many more ideas... 
