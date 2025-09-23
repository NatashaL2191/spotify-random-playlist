#=== Setup ===#
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import tkinter as tk

# Load environment variables from .env file
load_dotenv()

# Set up Spotify API credentials
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
SCOPE = "playlist-modify-public" 

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))
user = sp.current_user()
print("Logged in as:", user["display_name"])



def create_random_playlist(user_id, playlist_name, genres, trackcount):

    """
    Create a random Spotify playlist from given genres.
    
    user_id: Your Spotify username (string)
    playlist_name: Name of the playlist (string)
    genres: List of genres to pull songs from
    track_count: Number of songs in playlist
    """

    #create playlist
    playlist= sp.user_playlist_create(name=playlist_name, user=user_id, public=True)

 # Search for tracks in each genre
    all_tracks = []
    for genre in genres:
        results = sp.search(q=f'genre:"{genre}"', type='track', limit=50)
        tracks = [item['uri'] for item in results['tracks']['items']]
        all_tracks.extend(tracks)

 # Pick random tracks
    selected_tracks = random.sample(all_tracks, min(trackcount, len(all_tracks)))
    
    # Add tracks to playlist
    sp.playlist_add_items(playlist['id'], selected_tracks)
    
    print(f"Playlist '{playlist_name}' created with {len(selected_tracks)} random songs!")

    if len(all_tracks) < trackcount:
        print(f"Warning: Only {len(all_tracks)} tracks found for the given genre(s).")
        track_to_select = len(all_tracks)
    else:
        track_to_select = trackcount

    # Pick random tracks if tracks were found
    if all_tracks:
        selected_tracks = random.sample(all_tracks, track_to_select)
        
        # Add tracks to the new playlist
        sp.playlist_add_items(playlist['id'], selected_tracks)
        
        print(f"Playlist '{playlist_name}' created with {len(selected_tracks)} random songs!")
    else:
        print("No tracks found for the specified genres. No playlist was created.")

playlist_name = input("Enter Playlist Name: ")
genre = input("Enter Genre: ")
user_id = user['id']
create_random_playlist(user_id, playlist_name, genre, trackcount=20)

