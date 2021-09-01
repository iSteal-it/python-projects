import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

Client_ID =  "f805b6b9701043e290fd5dab4842e68a"
Client_Secret = "b4be5f4016204c0fb534dd18b94b918c"

sp = spotipy.Spotify(
auth_manager=SpotifyOAuth(
scope="playlist-modify-private",
redirect_uri="http://example.com",
client_id=Client_ID,
client_secret=Client_Secret,
show_dialog=True,
cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


date = input("please enter the date in yy-mm-dd format whos song you want: ")
response = requests.get(url=f"https://www.billboard.com/charts/billboard-global-200/{date}")
data = response.text

Soup = BeautifulSoup(data,"html.parser")
song_name = Soup.find_all(class_="item-details__title")
song_artist = Soup.find_all(class_="item-details__artist")

song_uris = []
year = date.split("-")[0]
for song in song_name:
    result = sp.search(q=f"track:{song.text} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

song_uris = song_uris[: len(song_uris) - 150]

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
