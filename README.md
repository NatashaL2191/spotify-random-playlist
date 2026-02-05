# Random Spotify Playlist Generator

This is a beginner Python project that uses the Spotify Web API to create a playlist of random songs from your saved tracks.

> Built and maintained by [@natashal2191](https://github.com/natashal2191)

---

## What It Does

- Logs into your Spotify account securely using OAuth
- Pulls a list of your liked (saved) tracks
- Randomly selects 10 songs
- Creates a public playlist with those tracks

---

## Tech Stack & Tools

- Python 3.x
- [Spotipy](https://spotipy.readthedocs.io/) (Spotify Web API wrapper)
- Git + GitHub for version control
- Spotify Developer Dashboard (for API credentials)
- Streamlit GUI

---
<pre><code>
## Project Structure

spotify-random-playlist/
├── .env                   # Your secret credentials (ignored by Git)
├── .gitignore             # Tells Git to ignore files like .env
├── README.md              # This file!
├── requirements.txt       # Dependencies for the project
├── random_playlist
</pre></code>
  
---
## Steps to Build This Project

### Step 1: Set Up a Spotify Developer App

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Click **"Create an App"**
3. Name your app and give it a short description
4. Add the following Redirect URI under **Edit Settings**: http://127.0.0.1:8888/callback
5. Copy your **Client ID** and **Client Secret** — you'll need these soon

---

### Step 2: Clone This Repository

<pre><code>
git clone https://github.com/natashal219/spotify-random-playlist.git
</pre></code>

### Step 3: Install Dependencies

<pre><code>
pip install -r requirements.txt
</pre></code>

### Step 4: Setup .env file
Fill out given credentials according to Spotify API

### Step 5: Run Python Script
To run GUI on browser run <pre><code>"streamlit run [file]"</pre></code> in bash terminal.


