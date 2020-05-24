import requests
import json
import urllib.request
import os

OFFSET_RANGE = 100


def saveAlbumCovers(file):
    """ 
    Saves album covers in './album_covers' folder from .json file.

    @param file: .json file containing song information 
        from Spotify API
    """
    with open(file) as f:
        data = json.load(f)
    for item in data.get("items"):
        album = item.get("track").get("album")
        img_url = album.get("images")[0].get("url")
        filename = album.get("name") + '.jpeg'
        print(filename)
        fullfilename = os.path.join('./album_covers', filename)
        urllib.request.urlretrieve(img_url, fullfilename)


def getSavedAlbumCovers():
    """
    Saves all albums that result from making a Spotify API call to get the 
    your Saved Tracks by making repeated API calls at varying offsets.
    """
    oauth_token = getOAuthToken()
    if not os.path.exists('./album_covers'):
        os.makedirs('./album_covers')
    for offset in range(OFFSET_RANGE):
        url = 'https://api.spotify.com/v1/me/tracks?limit=50&offset={}'.format(
            offset)
        response = requests.get(
            url, headers={'Authorization': 'Bearer {}'.format(oauth_token)})

        response_json = json.dumps(response.json(), indent=4)

        filename = 'saved-tracks.json'
        with open(filename, 'w') as f:
            print(response_json, file=f)

        saveAlbumCovers(filename)


def getOAuthToken():
    """ 
    Prompts user for OAuth Token.

    @return OAuth Token
    """
    oauth_token = input('Enter your OAuth Token: ')
    return oauth_token


getSavedAlbumCovers()
