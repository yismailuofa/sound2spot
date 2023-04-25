import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Replace with your own Spotify client ID and secret
redirect_uri = 'http://localhost:8000'

load_dotenv()

# Authentication
auth_manager = SpotifyOAuth(client_id=os.getenv('SPOTIFY_CLIENT_ID'),
                            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
                            redirect_uri=redirect_uri,
                            scope='playlist-modify-public')

sp = spotipy.Spotify(auth_manager=auth_manager)

# List of songs
songs = '''
Jazmine Sullivan - Mascara
Syd - Got Her Own
Jazmine Sullivan - Brand New
Jesse Boykins III - B4 The Night Is Thru (Syd Remix)
Marsha Ambrosius - With You
Solange - F.U.B.U. (feat. The-Dream & BJ The Chicago Kid)
Tweet - Magic
Alicia Keys - Fire We Make (feat. Maxwell)
Sonder - What You Heard
Chase Shakur - sink or swim
Lizzie Berchie - I Hope
Kelela - Waitin (Radio 1's Piano Sessions)
Drake - Flight's Booked
Jaz Karis - OPTION
Dayo Bello & Odeal - Outside
Venna, Yussef Dayes, & Marco Bernardis - Sicily' Box (feat. Rocco Palladino)
Jhene Aiko - Calm & Patient
Nao - It's You
Jessie Ware - Kind Of...Sometimes...Maybe
Teedra Moses - Beautiful Chaos
Lion Babe - Jungle Lady
Fatima - Note to Self
Iman Omari - Energy
Kelela - Send Me Out
Sade - No Ordinary Love
Erykah Badu - Didn't Cha Know
Jill Scott - A Long Walk
Lauryn Hill - Nothing Even Matters (feat. D'Angelo)
Avant - My First Love
Aaliyah - 4 Page Letter
'''

# Prompt for playlist title
title = "After Dark Episode 31"

# Split the list of songs into individual lines
song_list = songs.split('\n')


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
