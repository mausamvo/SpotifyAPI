import os

from sClient import SpotifyClient

#searching spotify for random songs 
def run():
    sClient = SpotifyClient('BQAbhi5yKR2fyQ1AEk70KMX3bFG7zJktRKcCXgO8J_wBLpP8HD7ObOxqbptd3NnZCtEW6FN79H-hKH87jraRREaWwKwTdTlajhtQMFRlJuuWfuk7uBbJTV6nBEOY0uyDcq1SWVNrcScrNK6FylIH6DPCoSRETl3gkFo2JMlpC2qz')
    randomSongs = sClient.searchRandomSongs()
    track_ids = [track['id'] for track in randomSongs] #list of song ids

#after getting the random songs, add them to the library 
    wasAdded = sClient.addSong(track_ids)
    if wasAdded:
        for track in randomSongs:
            print('Added ' +track['name']+ ' to your library')


if __name__ == "__main__":
    run()

