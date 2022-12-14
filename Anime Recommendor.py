

import requests
import pandas as pd
import warnings
from random import choice
warnings.filterwarnings("ignore")

#make API call
url = "https://api.jikan.moe/v4/anime"
r = requests.get(url).json()

#build dataframe
df = pd.DataFrame(columns=["anime_title", "genre", "total_eps", "rating_score", "anime_status"])


for anime in r["data"]:
    anime_title = anime['titles'][0]['title']
    genre = anime['genres'][0]['name']
    total_eps = anime['episodes']
    rating_score = anime['score']
    anime_status = anime['status']
    
#save data in pandas df
df = df.append({"anime_title": anime_title, "genre": genre, "total_eps": total_eps,
                  "rating_score": rating_score, "anime_status": anime_status},ignore_index=True)


df.head()

y = 'Name: ' + df.anime_title.astype(str) + '  Genre: ' + df.genre.astype(str) + '  Total eps: ' + df.total_eps.astype(str) + '  Status: ' + df.anime_status.astype(str) 

#anime choice
print(choice(y))

