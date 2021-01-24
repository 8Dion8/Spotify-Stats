import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()
SECRET = os.getenv('SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="fc75324c1ab44a2f915b28ca9da9de80",
                                               client_secret="YOUR_APP_CLIENT_SECRET",
                                               redirect_uri="YOUR_APP_REDIRECT_URI",
                                               scope="user-library-read"))