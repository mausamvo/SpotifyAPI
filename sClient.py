import random
import string
import urllib
import requests


class SpotifyClient(object):
    def __init__(self, apiKey):
        self.apiKey = apiKey

    def searchRandomSongs(self):
        wildcard = '%' + random.choice(string.ascii_lowercase) + '%'
        query = urllib.parse.quote(wildcard)
        offset = random.randint(0,2000)

        url = 'https://api.spotify.com/v1/search?q=' + query + '&offset=' + str(offset) + '&type=track'

        response = requests.get(
            url,
            headers={
                "Content": "application/json",
                "Authorization": "Bearer " + self.apiKey
            }
        )

        response_json = response.json()

        tracks = response_json['tracks']['items']

        print("Found " + str(len(tracks)) + " from your search")

        return tracks

    def addSong(self, track_ids):
        url = "https://api.spotify.com/v1/me/tracks"

        response = requests.put(
            url,
            headers={
                "Content": "application/json",
                "Authorization": "Bearer " + self.apiKey
            },
            json = {
                'ids' : track_ids
            }
        )

        return response.ok