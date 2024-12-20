import pandas as pd

df = pd.read_csv("./data/spotify.csv")
df.loc[815351:815360,'year'] = 2018

# print(df.head())
# print(df.describe())
# print(df.info())
#
# print(df['year'].unique())

df = df.drop(['id', 'album_id', 'artist_ids', 'track_number', 'disc_number', 'time_signature'], axis=1)
df['artists'] = df['artists'].str.strip("['']")
df['danceability'] = df['danceability'].round(2)
df['energy'] = df['energy'].round(2)
df['loudness'] = df['loudness'].round(2)
df['speechiness'] = df['speechiness'].round(2)
df['acousticness'] = df['acousticness'].round(2)
df['instrumentalness'] = df['instrumentalness'].round(2)
df['liveness'] = df['liveness'].round(2)
df['valence'] = df['valence'].round(2)
df["tempo"] = df["tempo"].astype(int)
df['year'] = df['year'].astype(str)
df["duration_s"] = (df["duration_ms"] / 1000).astype(int).round(0)

print(df.head())
