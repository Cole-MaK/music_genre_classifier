import spotipy
import pandas as pd
import numpy as np
import os
from spotipy.oauth2 import SpotifyOAuth

from getToken import *

token = get_token()

def search_song(token, search):
    url = f'https://api.spotify.com/v1/search?q=shelter+porter+robinson&type=track%2Cartist&limit=1'
def get_artist_id(token, search_name):
    url = f'https://api.spotify.com/v1/search?q=remaster%2520artist%3A{search_name}&type=artist&limit=1'
    header = get_auth_header(token)
    result = get(url, headers = header)
    json_result = json.loads(result.content)
    artist_id = json_result['artists']['items'][0]['id']
    return artist_id

def get_artist_top(token, id):
    url = f'https://api.spotify.com/v1/artists/{id}/top-tracks'
    header = get_auth_header(token)
    result = get(url, headers = header)
    json_result = json.loads(result.content)
    link = json_result['tracks'][0]['preview_url']
    print(link)
    

artist_id = get_artist_id(token, search_name=input('Artist to search:'))
get_artist_top(token, artist_id)