import requests
import json

API_KEY = "AIzaSyDEGPsu52rj2OKRk2SuuCfiZ-kALwgueHw"
CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():
    try:

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=ContentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        
        channel_items = data['Items'][0]
        channel_playlistID = channel_items['ContentDetails']['RelatedPlaylists']['Uploads']

        return channel_playlistID
    
    except requests.exceptions.RequestException as e:
        raise e
    
if __name__ == "main":
    get_playlist_id()