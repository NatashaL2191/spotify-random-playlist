# 🎧 Random Spotify Playlist Generator

This is a beginner Python project that uses the Spotify Web API to create a playlist of random songs from your saved tracks.

> Built and maintained by [@natashal219](https://github.com/natashal219)

---

## 🚀 What It Does

- Logs into your Spotify account securely using OAuth
- Pulls a list of your liked (saved) tracks
- Randomly selects 10 songs
- Creates a public playlist with those tracks

---

## 🧰 Tech Stack & Tools

- Python 3.x
- [Spotipy](https://spotipy.readthedocs.io/) (Spotify Web API wrapper)
- Git + GitHub for version control
- Spotify Developer Dashboard (for API credentials)

---

## 🧱 Steps to Build This Project

### 🔹 Step 1: Set Up a Spotify Developer App

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Click **"Create an App"**
3. Name your app and give it a short description
4. Add the following Redirect URI under **Edit Settings**: http://127.0.0.1:8888/callback
5. Copy your **Client ID** and **Client Secret** — you'll need these soon

---

### 🔹 Step 2: Clone This Repository

  <pre>
  ```bash
  git clone https://github.com/natashal219/spotify-random-playlist.git
  ```
  </pre>

### 🔹 Step 3: Install Dependencies
pip install spotipy python-dotenv

### 🔹 Step 4: Setup .env file

### 🔹 Step 5: Run Python Script


