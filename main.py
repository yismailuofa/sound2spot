import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

from soundcloud import getTitleAndTracks

# Replace with your own Spotify client ID and secret
redirect_uri = 'http://localhost:8000'

load_dotenv()

# Authentication
auth_manager = SpotifyOAuth(client_id=os.getenv('SPOTIFY_CLIENT_ID'),  # Change this to your own
                            # Change this to your own
                            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
                            redirect_uri=redirect_uri,
                            scope='playlist-modify-public')

sp = spotipy.Spotify(auth_manager=auth_manager)

# Change this to your own
URL = "https://soundcloud.com/g0homemasterpiece/after-dark-episode-31"

title, song_list = getTitleAndTracks(URL)

if title is None or song_list is None:
    print("Could not fetch url")
    exit(1)


def search_track(track_name):

    results = sp.search(q=track_name, type='track', limit=1)
    if results['tracks']['items']:
        print(f"Track found: {track_name}")
        return results['tracks']['items'][0]['id']
    else:
        print(f"Track not found: {track_name}")
        return None


# Search for the Spotify IDs of the tracks
track_ids = [search_track(song.strip()) for song in song_list if song]
track_ids = [id for id in track_ids if id is not None]


# Get the user's ID
user_id = sp.me()['id']

# Create the playlist
playlist = sp.user_playlist_create(
    user_id, title, public=True, description='')

# Add the tracks to the playlist
sp.playlist_add_items(playlist['id'], track_ids)

print(f"Playlist '{title}' created successfully!")
