#=== Setup ===#
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# Set up Spotify API credentials
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
SCOPE = os.getenv('SPOTIPY_SCOPE')

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))
user = sp.current_user()
print("Logged in as:", user["display_name"])



def create_random_playlist(user_id, playlist_name, genre, trackcount(20)):

    """
    Create a random Spotify playlist from given genres.
    
    user_id: Your Spotify username (string)
    playlist_name: Name of the playlist (string)
    genres: List of genres to pull songs from
    track_count: Number of songs in playlist
        """
    #create playlist
    playlist= sp.user_playlist_create(name=playlist_name, public=True, user=user_id)

 # Search for tracks in each genre
    all_tracks = []
    for genre in genres:
        results = sp.search(q=f'genre:"{genre}"', type='track', limit=50)
        tracks = [item['uri'] for item in results['tracks']['items']]
        all_tracks.extend(tracks)

 # Pick random tracks
    selected_tracks = random.sample(all_tracks, min(track_count, len(all_tracks)))
    
    # Add tracks to playlist
    sp.playlist_add_items(playlist['id'], selected_tracks)
    
    print(f"Playlist '{playlist_name}' created with {len(selected_tracks)} random songs!")