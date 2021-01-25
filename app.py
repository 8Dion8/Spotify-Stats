import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import json

load_dotenv()
SECRET = os.getenv('SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="fc75324c1ab44a2f915b28ca9da9de80",
                                               client_secret=SECRET,
                                               redirect_uri="https://www.google.it/",
                                               scope="user-read-recently-played"))

data = sp.current_user_recently_played(limit=50)

with open('data.json', 'w') as f:
    json.dump(data, f)


print(data)